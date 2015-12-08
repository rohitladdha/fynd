from django.conf.urls import patterns, url
from login_app import views

urlpatterns = patterns('',
    url(r'^login$', 'django.contrib.auth.views.login',name="login"),
    url(r'^login_api$', views.login_view,name="login_api"),
    url(r'^logout$', views.logout_view,name="logout"),
    url(r'^sample_view$', views.sample_view,name="sample_view"),
    url(r'test$', views.test, name='test_view'))