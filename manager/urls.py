# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'manager'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<id>\d+)/modify/$', views.modify, name='modify'),
    url(r'^(?P<id>\d+)/confirm/$', views.confirm, name='confirm'),
    url(r'^(?P<id>\d+)/delete/$', views.delete, name='delete'),
]