from django.db import models
from django.core.urlresolvers import reverse

from core.models import NflTeam, FieldPosition


class NflPlayer(models.Model):
	"""
	A Player that represents a Player that competes in the NFL
	and can be assigned to a fantasy team.
	"""

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	nfl_team = models.ForeignKey(NflTeam)
	position = models.ForeignKey(FieldPosition)

	def get_absolute_url(self):
		return reverse('player_detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return self.first_name + self.last_name


class NflSpecialTeam(models.Model):
	"""
	A Special/Defense team that represents an NFL Teams defensive
	or special team. Only used if the commisoner decides that 
	defensive players won't be picked.
	"""

	nfl_team = models.ForeignKey(NflTeam)

	def get_absolute_url(self):
		return reverse('special_team_detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return self.nfl_team