from django.db import models
from django.core.urlresolvers import reverse

# CONFERENCE CHOICES
AFC_CONFERENCE = 1
NFC_CONFERENCE = 2

CONFERENCE_CHOICES = (
	(AFC_CONFERENCE, 'AFC'),
	(NFC_CONFERENCE, 'NFC'),
	)
# END CONFERENCE CHOICES

# DIVISION CHOICES
NORTH, EAST, SOUTH, WEST = range(1, 5)

DIVISION_CHOICES = (
	(NORTH, 'North'),
	(EAST, 'East'),
	(SOUTH, 'South'),
	(WEST, 'West'),
	)

class NflTeam(models.Model):
	"""
	A Model that represents a team that competes in the NFL. Used
	to filter players.
	"""

	name = models.CharField(max_length=100)
	conference = models.PositiveIntegerField(choices=CONFERENCE_CHOICES)
	division = models.PositiveIntegerField(choices=DIVISION_CHOICES)

	def conference_str(self):
		return CONFERENCE_CHOICES[self.conference]

	def division_str(self):
		return DIVISION_CHOICES[self.divison]

	def get_absolute_url(self):
		return reverse('nfl_team_detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return self.name


class FieldPosition(models.Model):
	"""
	A Model that represents a field position on the NFL Field. Used
	to filter players.
	"""

	name = models.CharField(max_length=50)
	alias = models.CharField(max_length=10)

	def get_absolute_url(self):
		return reverse('field_position_detail', kwargs={'pk': self.pk})

	def __unicode__(self):
		return self.alias