__author__ = 'will'

from django.conf.urls import patterns, url
from feed import LatestEntriesFeed
import views


urlpatterns = patterns('',
   url(r'^latest/feed$', LatestEntriesFeed()),
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_id>\d+)/(?P<title>.*)$', views.view_post, name='Post'),

)

