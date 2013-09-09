from __future__ import unicode_literals

try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from rest_framework import routers

from .views import NflTeamViewSet, FieldPositionViewSet, UserViewSet, PermissionViewSet, GroupViewSet


core_router = routers.DefaultRouter(trailing_slash=False)
core_router.register(r'nflteam', NflTeamViewSet)
core_router.register(r'fieldposition', FieldPositionViewSet)
core_router.register(r'user', UserViewSet)
core_router.register(r'permission', PermissionViewSet)
core_router.register(r'group', GroupViewSet)

urlpatterns = patterns('',
					   url(r'^', include(core_router.urls)),
					  )