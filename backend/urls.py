from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('schedule', views.schedule, name='schedule'),
    path('job_portrait', views.job_portrait, name='job_portrait'),
    path('recommendation', views.recommendation, name='recommendation'),
]
