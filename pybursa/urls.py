from django.views.generic import TemplateView


from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^theme/$', TemplateView.as_view(template_name='theme.html'), name='theme'),
    url(r'^admin/', include(admin.site.urls)),
)
