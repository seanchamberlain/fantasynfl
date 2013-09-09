# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

import core.urls
import league.urls
import player.urls


urlpatterns = patterns('',
                       url(r'^core/', include(core.urls)),
                       url(r'^league/', include(league.urls)),
                       url(r'^player/', include(player.urls)),
                       )