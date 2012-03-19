from django.conf.urls.defaults import *
from django.views.generic import date_based
from blog.views import *

urlpatterns = patterns('',
    url(r'^$', blog_generic_view,
        {'redirect_to': list_detail.object_list}, name="blog_home"),
    url(r'^post/(?P<slug>[\w-]+)/$', blog_generic_view,
        {'redirect_to': list_detail.object_detail, 'slug_field': 'slug', 'paginate': False}, name="single_post"),
    url(r'^archive/(?P<month>[a-z-]+)/(?P<year>\d{4})/$', blog_generic_view,
        {'redirect_to': date_based.archive_month, 'date_field': 'published', 'template_name': 'blog/post_list.html'}),
#    url(r'^category/(\d+)/$', blog_posts_by_category, name="blog_posts_by_category"),
    url(r'^page/(?P<slug>[\w-]+)/$', page_detail, name="pages"),
    url(r'^novice/projekti/(\d+)/$', novice_by_projekt, name="novice_by_projekt"),
    #url(r'^kontakt/$', 'blog.views.kontakt', name="kontakt"),
)
