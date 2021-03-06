from django.views.generic import TemplateView

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^student', include('student.urls')),
    url(r'^coach', include('coaches.urls')),
    url(r'^course', include('courses.urls')),
    url(r'^address', include('address.urls')),
    url(r'^dossier', include('dossier.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',
        TemplateView.as_view(template_name='index.html'), name='index'),
)
