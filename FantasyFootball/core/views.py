from rest_framework import viewsets

from django.contrib.auth.models import User, Group, Permission

from .serializers import UserSerializer, GroupSerializer, PermissionSerializer


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