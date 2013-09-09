from rest_framework import serializers

from .models import NflPlayer, NflSpecialTeam, NflTeam, FieldPosition

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

class NflPlayerSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='nflplayer-detail')
    stringified = serializers.Field(source='__unicode__')

    class Meta:
        model = NflPlayer


class NflSpecialTeamSerializer(serializers.HyperlinkedModelSerializer):

	url = serializers.HyperlinkedIdentityField(
		view_name='nflspecialteam-detail')
	stringified = serializers.Field(source='__unicode__')

	class Meta:
		model = NflSpecialTeam