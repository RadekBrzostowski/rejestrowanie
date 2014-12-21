from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^/$', 'rej.views.home', name='rejestr'),
    url(r'^rej/$', 'rej.views.register_page', name='rejestr'),
)
