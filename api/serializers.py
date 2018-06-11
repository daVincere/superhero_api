from rest_framework import serializers

from .models import SuperHero

class SuperHeroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SuperHero
		fields = ["name", "real_name", "strength", "weapon", "location", "alive"]