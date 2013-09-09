from rest_framework import viewsets

from django.contrib.auth.models import User, Group, Permission
from .models import NflTeam, FieldPosition

from .serializers import NflTeamSerializer, FieldPositionSerializer, UserSerializer, GroupSerializer, PermissionSerializer

class NflTeamViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows NFL Teams to be viewed or edited.
    """
    queryset = NflTeam.objects.all()
    serializer_class = NflTeamSerializer


class FieldPositionViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Field Positions to be viewed or edited.
    """
    queryset = FieldPosition.objects.all()
    serializer_class = FieldPositionSerializer


class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer