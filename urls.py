import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.http import HttpResponseRedirect
import django.views.static
from django.contrib import admin
admin.autodiscover()

from djangopeople import views
from djangopeople.models import KungfuPerson



def redirect(url):
    return lambda res: HttpResponseRedirect(url)

from djangopeople.sitemaps import FlatPageSitemap, sitemap, CustomSitemap

sitemaps = {
    'flatpages': FlatPageSitemap,
    'otherpages': CustomSitemap,
}


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^stats/', include('stats.urls')),
                      
    (r'', include('djangopeople.urls')),
    (r'^newsletters/', include('newsletter.urls')),
    (r'^welcome/', include('welcome.urls')),
    (r'^twitter/', include('twitter.urls')),
                       
    (r'^sitemap.xml$', sitemap,
     {'sitemaps': sitemaps}),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': False
    }),
                       
)

if settings.DEBUG:
    
    # When not in debug mode (i.e. development mode)
    # nothing django.views.static.serve should not be used at all.
    # If it is used it means that nginx config isn't good enough.
    
    urlpatterns += patterns('', 
                            
        # CSS, Javascript and IMages
        (r'^webcam/(?P<path>.*)$', django.views.static.serve,
         {'document_root': settings.MEDIA_ROOT + '/webcam',
           'show_indexes': False}),                       
        (r'^img/(?P<path>.*)$', django.views.static.serve,
         {'document_root': settings.MEDIA_ROOT + '/img',
           'show_indexes': False}),                       
        (r'^css/(?P<path>.*)$', django.views.static.serve,
          {'document_root': settings.MEDIA_ROOT + '/css',
           'show_indexes': False}),
        (r'^js/(?P<path>.*)$', django.views.static.serve,
          {'document_root': settings.MEDIA_ROOT + '/js',
           'show_indexes': False}),
    
    )

