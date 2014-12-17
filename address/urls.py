from django.conf.urls import patterns, url

from address.views import address_list, address_item


urlpatterns = patterns('',
    url(r'^/(?P<address_id>\d+)/$', address_item, name="address_item"),
    url(r'^/$', address_list, name='address_list'),
    )
