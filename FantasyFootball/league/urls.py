from __future__ import unicode_literals

try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from rest_framework import routers

from .views import FantasyPlayerViewSet, FantasyTeamViewSet, FantasyLeagueViewSet, FantasyLeagueSettingsViewSet


league_router = routers.DefaultRouter(trailing_slash=False)
league_router.register(r'fantasyplayer', FantasyPlayerViewSet)
league_router.register(r'fantasyteam', FantasyTeamViewSet)
league_router.register(r'fantasyleague', FantasyLeagueViewSet)
league_router.register(r'fantasyleaguesettings', FantasyLeagueSettingsViewSet)

urlpatterns = patterns('',
					   url(r'^', include(league_router.urls)),
					  )