from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'form.views.home', name='home'),
    url(r'^create', 'form.views.create', name='create'),
    url(r'^events$', 'form.views.events', name='events'),
    url(r'^events/(?P<event_id>\d+)/$', 'form.views.detail', name='detail'),
    url(r'^categories', 'form.views.categories', name='categories'),
    # Examples:
    # url(r'^$', 'form.views.home', name='home'),
    # url(r'^form/', include('form.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
