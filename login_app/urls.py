from django.conf.urls import patterns, url
from login_app import views

urlpatterns = patterns('',
    url(r'^login_default/$', 'django.contrib.auth.views.login',name="my_login"),
    url(r'^login_view$', views.login_view,name="do_my_login"),
    url(r'^logout_view$', views.logout_view,name="do_my_login"),
    url(r'^sample_view$', views.sample_view,name="do_my_login"))