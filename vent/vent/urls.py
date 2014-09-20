__author__ = 'Jason Crockett'

from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from portfoilo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^$/contributers/', views.contributers,name='contributers')
)