from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from login_app import views

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/profile/$', auth_views.login),
  url(r'^auth/', include('login_app.urls')),
  url(r'^match/', include('matching_app.urls')),
  url(r'^',views.landing, name='landing_page'),
)
