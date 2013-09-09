from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import core.api.v0 as api_v0_urls

urlpatterns = patterns('',

	url(r'^api/v0/', include(api_v0_urls)),
    # Examples:
    # url(r'^$', 'FantasyFootball.views.home', name='home'),
    # url(r'^FantasyFootball/', include('FantasyFootball.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
