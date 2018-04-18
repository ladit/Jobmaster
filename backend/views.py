import json
import logging
from datetime import datetime

from django.http import JsonResponse
from django.conf import settings
from django.forms.models import model_to_dict

import django_rq

import jieba.posseg
import pandas as pd

from .models import Schedule, HandledJob
from .tasks import run
from . import recommend

logger = logging.getLogger('django')


# 处理求职者数据
def get_recommend(edu, dec, exp):
    seglist = jieba.posseg.cut(dec)
    vec = recommend.dec.copy()
    kword = set()
    for seg in seglist:
        word = "".join(seg.word).strip().lower()
        if word == 'ai': word = '人工智能'
        if word == '后台': word = '后端'
        if word == '分析员': word = '分析师'
        if word == '美工': word = 'ui'
        if word == 'nlp': word = '自然语言'
        if word in recommend.dec_keyword:
            kword.add(word)
            vec[word] = [1]
    ans = pd.DataFrame(vec)
    worker = list(kword)
    # pre = recommend.RFCModel.predict(ans[recommend.dec_keyword][0:])
    # kind = str(pre[0])
    kind = '117'
    ans = {}
    try:
        hj = HandledJob.objects.filter(job_class=kind)
        for job in hj:
            if job.job_dec is None: continue
            decword = "".join(job.job_dec).split()
            ans[job.id] = recommend.DocModel.n_similarity(worker, decword)
    except Exception as err:
        logger.debug("get recommend ERROR: ")
        print(err)
    p = sorted(ans.items(), key=lambda ans: ans[1], reverse=True)
    cas = 0
    response = []
    for (id, pi) in p:
        if cas > 10: break
        response.append([id, pi])
        cas += 1
    return response


def login(request):
    if request.method == 'POST':
        request_json = json.loads(request.body.decode('utf-8'))
        if 'username' in request_json \
                and 'password' in request_json \
                and request_json['username'] == settings.ADMIN_USERNAME \
                and request_json['password'] == settings.ADMIN_PASSWORD:
            response = {
                'error': 0,
                'message': 'auth success'
            }
            return JsonResponse(response)
        response = {
            'error': -1,
            'message': 'auth failed'
        }
        return JsonResponse(response)


def schedule(request):
    # get schedule status
    if request.method == 'GET':
        try:
            latest_schedule = Schedule.objects.latest('id')
        except Schedule.DoesNotExist:
            websites = ['boss', 'job51', 'liepin', 'neitui', 'zlzp']
            websites_string = ','.join(websites)
            new_schedule = Schedule(websites=websites_string)
            new_schedule.save()
            django_rq.enqueue(run, args=[websites], job_id='init')
            response = {
                'error': 1,
                'message': 'need init'
            }
            return JsonResponse(response)
        else:
            all_schedules = list(Schedule.objects.all().values())
            if latest_schedule.finish_time is None:
                response = {
                    'error': 2,
                    'message': 'latest task not finished',
                    'schedule': all_schedules
                }
                return JsonResponse(response)
            else:
                response = {
                    'error': 0,
                    'message': 'allow operation',
                    'schedule': all_schedules
                }
                return JsonResponse(response)

    # modify schedule
    if request.method == 'PUT':
        request_json = json.loads(request.body.decode('utf-8'))
        if 'websites' in request_json \
                and 'every_x_days' in request_json \
                and 'every_x_clock' in request_json:
            scheduler = django_rq.get_scheduler('default')
            scheduled_jobs = scheduler.get_jobs()
            for job in scheduled_jobs:
                scheduler.cancel(job)
            utc_now = datetime.utcnow()
            year = int(utc_now.strftime('%Y'))
            month = int(utc_now.strftime('%m'))
            day = int(utc_now.strftime('%d'))
            first_time = datetime(year, month, day, request_json['every_x_clock'])
            if first_time < utc_now:
                first_time = datetime(year, month, day + 1, request_json['every_x_clock'])
            scheduler.schedule(scheduled_time=first_time,
                               func=run,
                               args=[request_json['websites']],
                               interval=86400 * request_json['every_x_days']
                               )
            # 记录到数据库
            websites_string = ','.join(request_json['websites'])
            new_schedule = Schedule(websites=websites_string,
                                    every_x_days=request_json['every_x_days'],
                                    every_x_clock=request_json['every_x_clock'])
            new_schedule.save()
            response = {
                'error': 0,
                'message': 'done',
                'schedule': model_to_dict(new_schedule)
            }
            return JsonResponse(response)
        response = {
            'error': 400,
            'message': 'bad input'
        }
        return JsonResponse(response)


def job_portrait(request):
    if request.method == 'POST':
        request_json = json.loads(request.body.decode('utf-8'))
        if 'job_show_name' in request_json:
            hj = HandledJob.objects.filter(job_show_name=request_json['job_show_name']).order_by('job_exp')
            dec_list = {}
            payment_distribution = {'面议': 0, '0-5000': 0, '5000-10000': 0, '10000-25000': 0, '25000-50000': 0,
                                    '50000-80000': 0, '80000+': 0}
            company_size_distribution = {'0-100': 0, '100-800': 0, '800-2000': 0, '2000-8000': 0, '8000-20000': 0,
                                         '20000+': 0}
            edu_demand = {}
            workplaces = {}
            for job in hj:
                if job.job_min_edu in edu_demand:
                    edu_demand[job.job_min_edu] += 1
                else:
                    edu_demand.update({job.job_min_edu: 1})

                if job.job_workplace in workplaces:
                    workplaces[job.job_workplace] += 1
                else:
                    workplaces.update({job.job_workplace: 1})

                if job.job_pay == 0:
                    payment_distribution['面议'] += 1
                elif 0 < job.job_pay <= 5000:
                    payment_distribution['0-5000'] += 1
                elif 5000 < job.job_pay <= 10000:
                    payment_distribution['5000-10000'] += 1
                elif 10000 < job.job_pay <= 25000:
                    payment_distribution['10000-25000'] += 1
                elif 25000 < job.job_pay <= 50000:
                    payment_distribution['25000-50000'] += 1
                elif 50000 < job.job_pay <= 80000:
                    payment_distribution['50000-80000'] += 1
                elif 80000 < job.job_pay:
                    payment_distribution['80000+'] += 1

                if 0 < job.company_size <= 100:
                    company_size_distribution['0-100'] += 1
                elif 100 < job.company_size <= 800:
                    company_size_distribution['100-800'] += 1
                elif 800 < job.company_size <= 2000:
                    company_size_distribution['800-2000'] += 1
                elif 2000 < job.company_size <= 8000:
                    company_size_distribution['2000-8000'] += 1
                elif 8000 < job.company_size <= 20000:
                    company_size_distribution['8000-20000'] += 1
                elif 20000 < job.company_size:
                    company_size_distribution['20000+'] += 1

                dec = job.job_dec.split(' ')
                for item in dec:
                    if item in dec_list:
                        dec_list[item] += 1
                    else:
                        dec_list.update({item: 1})
                sorted_dec = sorted(dec_list.items(), key=lambda x: x[1], reverse=True)
                i = 0
                dec_words = {}
                for (item, count) in sorted_dec:
                    if i > 10: break
                    dec_words.update({item: count})
                    i += 1
            response = {
                'error': 0,
                'job_show_name': request_json['job_show_name'],
                'least_exp': hj[0].job_exp,
                'dec': dec_words,
                'edu_demand_distribution': edu_demand,
                'payment_distribution': payment_distribution,
                'company_size_distribution': company_size_distribution,
                'workplace_distribution': workplaces,
            }
            return JsonResponse(response)
        response = {
            'error': 400,
            'message': 'bad input'
        }
        return JsonResponse(response)


def recommendation(request):
    if request.method == 'POST':
        request_json = json.loads(request.body.decode('utf-8'))
        if 'edu' in request_json \
                and 'workplace' in request_json \
                and 'exp' in request_json \
                and 'skill' in request_json \
                and 'major' in request_json \
                and 'job_show_name' in request_json:
            dec = request_json['skill'] + '+' + request_json['major'] + '+' + request_json['job_show_name']
            hj = HandledJob.objects.filter(job_show_name=request_json['job_show_name'])
            payment_list = []
            edu_list = []
            exp_list = []
            no_edu_demand_count = 0
            for job in hj:
                payment_list.append(job.job_pay)
                exp_list.append(job.job_exp)
                if job.job_min_edu != 0:
                    edu_list.append(job.job_min_edu)
                else:
                    no_edu_demand_count += 1
            recommendations = get_recommend(request_json['edu'], dec, request_json['exp'])
            recommend_jobs = []
            pay_sum = 0
            for recommendation in recommendations:
                recommend_job = {}
                id = recommendation[0]
                job = HandledJob.objects.get(id=id)
                recommend_job['company_name'] = job.company_name
                recommend_job['payment'] = job.job_pay
                pay_sum += job.job_pay
                recommend_job['welfare'] = job.company_welfare
                recommend_job['size'] = job.company_size
                recommend_job['url'] = job.job_url
                recommend_job['rate'] = recommendation[1]
                recommend_jobs.append(recommend_job)
            personal_payment = pay_sum / len(recommendations)
            response = {
                'error': 1,
                'job_show_name': request_json['job_show_name'],
                'payment_range': str(min(payment_list)) + '-' + str(max(payment_list)),
                'personal': {
                    'payment': personal_payment,
                    'edu': request_json['edu'],
                    'exp': request_json['exp'],
                },
                'average': {
                    'payment': sum(payment_list) / float(len(payment_list)),
                    'edu': sum(edu_list) / float(len(edu_list)),
                    'exp': sum(exp_list) / float(len(exp_list)),
                    'no_edu_demand_count': no_edu_demand_count,
                },
                'jobs': recommend_jobs,
            }
            return JsonResponse(response)
        response = {
            'error': 400,
            'message': 'bad input'
        }
        return JsonResponse(response)
