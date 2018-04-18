from django.db import models


class Schedule(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True, blank=True)
    websites = models.CharField(max_length=200)
    every_x_days = models.IntegerField(default=-1)
    every_x_clock = models.IntegerField(default=-1)
    finish_count = models.IntegerField(default=0)


class Job(models.Model):
    job_name = models.TextField()  # 工作名称
    job_show_name = models.TextField(null=True)  # 岗位统一名
    job_class = models.IntegerField(null=True, default=-9)  # 岗位分类结果
    job_issue = models.TextField(null=True)  # 工作来源 zlzp、51job等
    job_url = models.TextField(null=True)  # 工作详情页链接
    job_pay = models.TextField(null=True)  # 工资
    job_workplace = models.TextField(null=True)  # 工作地点
    job_min_edu = models.TextField(null=True)  # 最低学历
    job_exp = models.TextField(null=True)  # 工作经验
    job_dec = models.TextField(null=True)  # 工作描述（技能提取）
    company_name = models.TextField(null=True)  # 公司名称
    company_ind = models.TextField(null=True)  # 公司行业
    company_size = models.TextField(null=True)  # 公司规模
    company_welfare = models.TextField(null=True)  # 公司福利


class HandledJob(models.Model):
    job_name = models.TextField()
    job_show_name = models.TextField(null=True)
    job_class = models.IntegerField(null=True, default=-9)
    job_issue = models.TextField(null=True)
    job_url = models.TextField()
    job_pay = models.IntegerField(null=True, default=-9)
    job_workplace = models.IntegerField(null=True, default=-9)
    job_min_edu = models.IntegerField(null=True, default=-9)
    job_exp = models.IntegerField(null=True, default=-9)
    job_dec = models.TextField(null=True)
    company_name = models.TextField(null=True)
    company_ind = models.TextField(null=True)
    company_size = models.IntegerField(null=True, default=-9)
    company_welfare = models.TextField(null=True)
