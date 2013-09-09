from rest_framework import serializers

from .models import NflPlayer, NflSpecialTeam 

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