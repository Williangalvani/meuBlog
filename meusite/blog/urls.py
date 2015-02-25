__author__ = 'will'

from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/$', views.view_post, name='Post'),
)