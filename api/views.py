# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import SuperHero
from .serializers import SuperHeroSerializer

from rest_framework import generics

# Create your views here.
class CreateHero(generics.CreateAPIView):
	queryset = SuperHero.objects.all()
	serializer_class = SuperHeroSerializer

class ListHeroes(generics.ListAPIView):
	queryset = SuperHero.objects.all()
	serializer_class = SuperHeroSerializer

class HeroDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = SuperHero.objects.all()
	serializer_class = SuperHeroSerializer

