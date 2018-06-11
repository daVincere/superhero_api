# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SuperHero(models.Model):
	name = models.CharField(max_length=150)
	real_name = models.CharField(max_length=150)

	strength = models.CharField(max_length=250)
	weapon = models.CharField(max_length=300)
	
	location = models.CharField(max_length=300)

	UNIVERSE = (
				('Marvel', 'Marvel'),
				('DC', 'DC'),
				('Other','Miscellaneous'),
			)
	universe = models.CharField(max_length=10, choices=UNIVERSE)

	alive = models.BooleanField(default=True)


	def __str__(self):
		return self.name