from django.conf.urls import patterns, include, url
from matchApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'))
)
