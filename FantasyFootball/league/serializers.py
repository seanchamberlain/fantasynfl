from rest_framework import serializers

from .models import FantasyPlayer, FantasyTeam, FantasyLeague, FantasyLeagueSettings

class FantasyPlayerSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='fantasyplayer-detail')
    stringified = serializers.Field(source='__unicode__')

    class Meta:
        model = FantasyPlayer


class FantasyTeamSerializer(serializers.HyperlinkedModelSerializer):

	url = serializers.HyperlinkedIdentityField(
		view_name='fantasyteam-detail')
	stringified = serializers.Field(source='__unicode__')

	class Meta:
		model = FantasyTeam


class FantasyLeagueSerializer(serializers.HyperlinkedModelSerializer):

	url = serializers.HyperlinkedIdentityField(
		view_name='fantasyleague-detail')
	stringified = serializers.Field(source='__unicode__')

	class Meta:
		model = FantasyLeague


class FantasyLeagueSettingsSerializer(serializers.HyperlinkedModelSerializer):

	url = serializers.HyperlinkedIdentityField(
		view_name='fantasyleaguesettings-detail')
	# stringified = serializers.Field(source='__unicode__')

	class Meta:
		model = FantasyLeagueSettings