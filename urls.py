from django.conf.urls.defaults import patterns, include, url
from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^fotogalerija/', include('imagestore.urls', namespace='imagestore')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^', include('blog.urls')),
    url(r'^', include('projekti.urls')),
)
