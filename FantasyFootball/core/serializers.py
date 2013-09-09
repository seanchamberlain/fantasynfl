from rest_framework import serializers

from django.contrib.auth.models import User, Group, Permission
from .models import NflTeam, FieldPosition

class NflTeamSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='nflteam-detail')
    stringified = serializers.Field(source='__unicode__')

    class Meta:
        model = NflTeam


class FieldPositionSerializer(serializers.HyperlinkedModelSerializer):

	url = serializers.HyperlinkedIdentityField(
		view_name='fieldposition-detail')
	stringified = serializers.Field(source='__unicode__')

	class Meta:
		model = FieldPosition


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
