from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateHero, ListHeroes, HeroDetail

urlpatterns = [
    url(r'^', ListHeroes.as_view(), name="list_heroes"),
    url(r'^add/$', CreateHero.as_view(), name="add_heroes"),
    url(r'^hero/(?P<pk>[0-9]+)/$', HeroDetail.as_view(), name="hero_detail"),
]
