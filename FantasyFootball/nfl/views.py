from rest_framework import viewsets

from .models import NflPlayer, NflSpecialTeam, NflTeam, FieldPosition

from .serializers import NflPlayerSerializer, NflSpecialTeamSerializer, NflTeamSerializer, FieldPositionSerializer


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


class NflPlayerViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows NFL Players to be viewed or edited.
    """
    queryset = NflPlayer.objects.all()
    serializer_class = NflPlayerSerializer


class NflSpecialTeamViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows NFL Special Teams to be viewed or edited.
    """
    queryset = NflSpecialTeam.objects.all()
    serializer_class = NflSpecialTeamSerializer