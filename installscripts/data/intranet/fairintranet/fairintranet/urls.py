import os

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from technicians import urls as technician_urls


urlpatterns = patterns('',
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^download/movie/(\d+)/$', 'core.views.download_movie', name='download_movie'),
    url(r'^download/ebook/(\d+)/$', 'core.views.download_ebook', name='download_ebook'),
    url(r'^download/external-collection/(\d+)/$', 'core.views.download_external_collection', name='download_external_collection'),
    url(r'^technicians/', include(technician_urls, namespace='technicians')),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'', include(wagtail_urls)),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
