from django.conf.urls import patterns, include, url
from matchApp import views

urlpatterns = patterns('',
    #url[0]: regex that matches empty string
    #url[1]: for any url that matches this pattern, invoke view views.index
    #url[2]: optional parameter name
    url(r'^$', views.index, name='index'),

    url(r'^about/', views.about, name='about')
)
