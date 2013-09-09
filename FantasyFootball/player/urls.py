from __future__ import unicode_literals

try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from rest_framework import routers

from .views import NflPlayerViewSet, NflSpecialTeamViewSet


player_router = routers.DefaultRouter(trailing_slash=False)
player_router.register(r'nflplayer', NflPlayerViewSet)
player_router.register(r'nflspecialteam', NflSpecialTeamViewSet)

urlpatterns = patterns('',
					   url(r'^', include(player_router.urls)),
					  )