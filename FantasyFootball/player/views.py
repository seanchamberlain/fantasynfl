from rest_framework import viewsets

from .models import NflPlayer, NflSpecialTeam

from .serializers import NflPlayerSerializer, NflSpecialTeamSerializer

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