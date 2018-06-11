from django import forms

from api.models import SuperHero

class SuperHeroForm(forms.ModelForm):
	class Meta:
		model = SuperHero
		fields =  ["name", "real_name", "strength", "weapon", "location", "universe", "alive"]