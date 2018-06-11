# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import SuperHero

class SuperHeroAdmin(admin.ModelAdmin):
	class Meta:
		model = SuperHero
		fields = ["name", "real_name", "strength", "weapon", "location", "universe", "alive"]

admin.site.register(SuperHero, SuperHeroAdmin)