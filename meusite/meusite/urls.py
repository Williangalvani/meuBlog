from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.index'),

    url(r'^apps/italia/', include('italia.urls')),

    url(r'^apps/$', 'blog.views.apps_index'),

    url(r'^admin/', include(admin.site.urls)),

    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
      + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
