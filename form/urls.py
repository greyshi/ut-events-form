from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from form.api import EventResource, CategoryResource

admin.autodiscover()
v1_api = Api(api_name='v1')
v1_api.register(EventResource())
v1_api.register(CategoryResource())

urlpatterns = patterns('',
    url(r'^$', 'form.views.home', name='home'),
    url(r'^create/', 'form.views.create', name='create'),
    url(r'^events/$', 'form.views.events', name='events'),
    url(r'^events/(?P<event_id>\d+)/$', 'form.views.detail', name='detail'),
    url(r'^confirm/', 'form.views.confirm', name='confirm'),
    url(r'^android/', 'form.views.android', name='android'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
