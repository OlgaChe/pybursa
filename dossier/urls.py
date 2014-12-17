from django.conf.urls import patterns, url

from dossier.views import dossier_list, dossier_item


urlpatterns = patterns('',
    url(r'^/(?P<dossier_id>\d+)/$', dossier_item, name="dossier_item"),
    url(r'^/$', dossier_list, name='dossier_list'),
    )
