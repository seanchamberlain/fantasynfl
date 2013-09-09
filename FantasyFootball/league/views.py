from rest_framework import viewsets

from .models import FantasyPlayer, FantasyTeam, FantasyLeague, FantasyLeagueSettings

from .serializers import FantasyPlayerSerializer, FantasyTeamSerializer, FantasyLeagueSerializer, FantasyLeagueSettingsSerializer

class FantasyPlayerViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows a Fantasy Player to be viewed or edited.
    """
    queryset = FantasyPlayer.objects.all()
    serializer_class = FantasyPlayerSerializer


class FantasyTeamViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Fantasy Team to be viewed or edited.
    """
    queryset = FantasyTeam.objects.all()
    serializer_class = FantasyTeamSerializer


class FantasyLeagueViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Fantasy League to be viewed or edited.
    """
    queryset = FantasyLeague.objects.all()
    serializer_class = FantasyLeagueSerializer


class FantasyLeagueSettingsViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows Fantasy League Settings to be viewed or edited.
    """
    queryset = FantasyLeagueSettings.objects.all()
    serializer_class = FantasyLeagueSettingsSerializer