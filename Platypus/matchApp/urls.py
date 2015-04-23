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
	url(r'^selectsection_CSCI1310/$', views.selectsection_CSCI1310, name='1310'),
	url(r'^selectsection_CSCI2270/$', views.selectsection_CSCI2270, name='2270'),
	url(r'^selectsection_CSCI2400/$', views.selectsection_CSCI2400, name='2400'),
	url(r'^selectsection_CSCI2820/$', views.selectsection_CSCI2820, name='2820'),
	url(r'^selectsection_CSCI2824/$', views.selectsection_CSCI2824, name='2824'),
	url(r'^selectsection_CSCI3104/$', views.selectsection_CSCI3104, name='3104'),
	url(r'^selectsection_CSCI3155/$', views.selectsection_CSCI3155, name='3155'),
	url(r'^selectsection_CSCI3308/$', views.selectsection_CSCI3308, name='3308'),
	url(r'^selectsection_CSCI3753/$', views.selectsection_CSCI3753, name='3753'),

	url(r'^add1300001/$', views.add1300001, name='add1300001'),
	url(r'^add1300002/$', views.add1300002, name='add1300002'),
	url(r'^add1300003/$', views.add1300003, name='add1300003'),

	url(r'^add1310001/$', views.add1310001, name='add1310001'),
	url(r'^add1310002/$', views.add1310002, name='add1310002'),
	url(r'^add1310003/$', views.add1310003, name='add1310003'),

	url(r'^add2270001/$', views.add2270001, name='add2270001'),
	url(r'^add2270002/$', views.add2270002, name='add2270002'),
	url(r'^add2270003/$', views.add2270003, name='add2270003'),

	url(r'^add2400001/$', views.add2400001, name='add2400001'),
	url(r'^add2400002/$', views.add2400002, name='add2400002'),
	url(r'^add2400003/$', views.add2400003, name='add2400003'),

	url(r'^add2820001/$', views.add2820001, name='add2820001'),
	url(r'^add2820002/$', views.add2820002, name='add2820002'),
	url(r'^add2820003/$', views.add2820003, name='add2820003'),

	url(r'^add2824001/$', views.add2824001, name='add2824001'),
	url(r'^add2824002/$', views.add2824002, name='add2824002'),
	url(r'^add2824003/$', views.add2824003, name='add2824003'),

	url(r'^add3104001/$', views.add3104001, name='add3104001'),
	url(r'^add3104002/$', views.add3104002, name='add3104002'),
	url(r'^add3104003/$', views.add3104003, name='add3104003'),

	url(r'^add3155001/$', views.add3155001, name='add3155001'),
	url(r'^add3155002/$', views.add3155002, name='add3155002'),
	url(r'^add3155003/$', views.add3155003, name='add3155003'),

	url(r'^add3308001/$', views.add3308001, name='add3308001'),
	url(r'^add3308002/$', views.add3308002, name='add3308002'),
	url(r'^add3308003/$', views.add3308003, name='add3308003'),

	url(r'^add3753001/$', views.add3753001, name='add3753001'),
	url(r'^add3753002/$', views.add3753002, name='add3753002'),
	url(r'^add3753003/$', views.add3753003, name='add3753003'))