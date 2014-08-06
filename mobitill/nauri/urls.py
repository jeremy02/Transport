from django.conf.urls import patterns, url
from nauri import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^device_register/$', views.device_register, name='device_register'),
        url(r'^client_register/$', views.client_register, name='client_register'),
        url(r'^search_device/$', views.search_device, name='search_device'),
        url(r'^search_client/$', views.search_client, name='search_client'),
        url(r'^client_device_assign/$', views.client_device_assign, name='client_device_assign'),
        url(r'^load_device_list/$', views.load_device_list, name='load_device_list'),
        )

#urlpatterns = patterns('pos_app.views',

#)
