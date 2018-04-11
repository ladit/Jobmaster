from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('schedule', views.schedule, name='schedule'),
    path('init', views.init, name='init'),
]