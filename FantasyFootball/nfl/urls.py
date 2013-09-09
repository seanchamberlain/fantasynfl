from __future__ import unicode_literals

try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from rest_framework import routers

from .views import NflPlayerViewSet, NflSpecialTeamViewSet, NflTeamViewSet, FieldPositionViewSet


nfl_router = routers.DefaultRouter(trailing_slash=False)
nfl_router.register(r'nflteam', NflTeamViewSet)
nfl_router.register(r'fieldposition', FieldPositionViewSet)
nfl_router.register(r'nflplayer', NflPlayerViewSet)
nfl_router.register(r'nflspecialteam', NflSpecialTeamViewSet)

urlpatterns = patterns('',
					   url(r'^', include(nfl_router.urls)),
					  )