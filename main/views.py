# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from main.forms import SuperHeroForm

# Create your views here.
def superhero_entry(request):
	"""
		This makes sure that the form accpets a POST requests (of some data) or Nothing.
		Without this the form would even accept empty totos.
	"""
	# if not request.user.is_authenticated():
	# 	raise Http404

	form = SuperHeroForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Aapke hero bana diya gaya hai!")
		return HttpResponseRedirect("/")
	else:
		messages.error(request, "Tehro! Error hua hai.", extra_tags="") 
	context = {
		'title': "Create",
		'form' : form,
	}
	return render(request, 'base.html', context)