# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'manager'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detailview/(?P<id>.+)/$', views.detail, name='detail'),
    url(r'^modify/(?P<id>./d+)/$', views.modify, name='modify'),
    url(r'^delete/(?P<id>./d+)/$', views.delete, name='delete'),
]