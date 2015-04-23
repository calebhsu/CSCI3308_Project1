""" Ensures that all pages created link together properly.
Pages included: index, home, class page, registration page, login page, and logout screen. 
"""

from django.conf.urls import patterns, url
from matchApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^classpage/$', views.classpage, name='classpage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^addcourses/$', views.addcourses, name='addcourses'),
	url(r'^selectsection_CSCI1300/$', views.selectsection_CSCI1300, name='1300'),
	url(r'^add1300001/$', views.add1300001, name='add1300001'))