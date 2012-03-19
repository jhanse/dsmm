from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^projekti/$', 'projekti.views.index', name="projekti"),
    url(r'^projekt/(?P<slug>[\w-]+)/$', 'projekti.views.detail', name="projekt_detail"),
)