from django.conf.urls import patterns, url
from matchApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='login'),
    url(r'^home/$', views.home, name='home'))