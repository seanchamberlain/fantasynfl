from rest_framework import serializers

from django.contrib.auth.models import User, Group, Permission


class UserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail')
    stringified = serializers.Field(source='__unicode__')

    class Meta:
        model = User
        exclude = ('password',)     # API should be behind auth, but caution


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='group-detail')
    stringified = serializers.Field(source='__unicode__')

    class Meta:
        model = Group


class PermissionSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='permission-detail')
    stringified = serializers.Field(source='__unicode__')

    class Meta:
        model = Permission
