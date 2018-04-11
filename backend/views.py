import json
from builtins import list

from django.http import JsonResponse
from django.conf import settings
from django.forms.models import model_to_dict

from .models import Schedule, Job, HandledJob


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
            first_schedule = Schedule.objects.get(pk=1)
        except Schedule.DoesNotExist:
            response = {
                'error': 1,
                'message': 'need init'
            }
            return JsonResponse(response)
        else:
            latest_schedule = Schedule.objects.latest('id')
            if latest_schedule.finish_time is None:
                response = {
                    'error': 2,
                    'message': 'latest task not finished'
                }
                return JsonResponse(response)
            else:
                all_schedules = list(Schedule.objects.all().values())
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
            websites_string = ','.join(request_json['websites'])
            new_schedule = Schedule(websites=websites_string, every_x_days=request_json['every_x_days'],
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


def init(request):
    # do something
    response = {
        'error': 0,
        'message': 'initializing'
    }
    return JsonResponse(response)
