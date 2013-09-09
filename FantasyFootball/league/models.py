from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from nfl.models import NflPlayer, NflSpecialTeam, FieldPosition


class FantasyPlayer(models.Model):
	"""
	A NFL Player that represents a Member of a Fantasy Team
	"""

	nfl_player = models.ForeignKey(NflPlayer)
	position_on_team = models.ForeignKey(FieldPosition)

	def get_absolute_url(self):
		return reverse('fantasy_player_detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return self.nfl_player


class FantasyLeagueSettings(models.Model):
	"""
	Settings that define a Fantasy League
	"""

	num_of_players = models.PositiveIntegerField(max_length=2)
	defensive_players = models.BooleanField()

	def get_absolute_url(self):
		return reverse('fantasy_league_settings_detail', kwargs={'pk': self.pk})


class FantasyTeam(models.Model):
	"""
	A Fantasy Team represents a team within a Fantasy League
	"""

	owner = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	players = models.ManyToManyField(NflPlayer)
	special_team = models.ManyToManyField(NflSpecialTeam)

	def get_absolute_url(self):
		return reverse('fantasy_team_detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return self.team_name


class FantasyLeague(models.Model):
	"""
	A Fantasy League
	"""

	name = models.CharField(max_length=100)
	commissioner = models.ForeignKey(User)
	settings = models.OneToOneField(FantasyLeagueSettings)
	teams = models.ForeignKey(FantasyTeam)

	def get_absolute_url(self):
		return reverse('fantasy_league_detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return self.league_name