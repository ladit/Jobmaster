from django.db import models


class Schedule(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True, blank=True)
    finish_count = models.IntegerField(default=0)
    websites = models.CharField(max_length=200)
    every_x_days = models.IntegerField(default=-1)
    every_x_clock = models.IntegerField(default=-1)


class Job(models.Model):
    job_name = models.TextField()  # 工作名称
    job_pay = models.TextField()  # 工资
    job_workplace = models.TextField()  # 工作地点
    job_dec = models.TextField()  # 工作描述（技能提取）
    job_min_edu = models.TextField()  # 最低学历
    job_exp = models.TextField()  # 工作经验
    company_welfare = models.TextField()  # 公司福利
    company_name = models.TextField()  # 公司名称
    company_ind = models.TextField()  # 公司行业
    company_size = models.TextField()  # 公司规模
    job_url = models.TextField()  # 工作详情页链接
    job_issue = models.TextField()  # 工作来源 zlzp、51job等


class HandledJob(models.Model):
    job_name = models.TextField()
    job_pay = models.IntegerField(default=-1)
    job_workplace = models.IntegerField(default=-1)
    job_dec = models.TextField()
    job_min_edu = models.IntegerField(default=-9)
    job_exp = models.IntegerField(default=-9)
    company_welfare = models.TextField()
    company_name = models.TextField()
    company_ind = models.TextField()
    company_size = models.TextField()
    job_url = models.TextField()
    job_issue = models.TextField()
