from django.conf.urls import patterns, url
from matching_app import views

urlpatterns = patterns('',
    url(r'^get_intersection$', views.get_intersection,name="get_intersection"),)
