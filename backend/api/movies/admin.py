from django.contrib import admin
from movies.models import Movie, Review, Actor


admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Actor)
