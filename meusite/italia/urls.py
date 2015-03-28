__author__ = 'will'

from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^clear$', views.clear, name='clear'),
    url(r'^view/(?P<name>\w+)$', views.viewDownload, name="Results"),
    url(r'^view/(?P<name>\w+)/raw$', views.viewDownloadRaw, name="ResultsRaw"),
#    url(r'^post/(?P<post_id>\d+)/(?P<title>.*)$', views.view_post, name='Post'),
)

