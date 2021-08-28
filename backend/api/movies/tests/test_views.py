from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from movies.models import Movie
from movies.models import Actor
from movies.models import Review
from collections import OrderedDict


class MoviesViewsTests(APITestCase):
    """
    Test movies views.
    """

    def setUp(self):
        self.actor = Actor.objects.create(
            first_name="Uma", last_name="Thurman")
        self.movie = Movie.objects.create(
            title="Kill Bill", description="Fight movie")
        Movie.objects.create(title="Kill Bill 2",
                             description="Fight movie")
        Movie.objects.create(title="Lord of the ring 1",
                             description="Aventure")
        Movie.objects.create(title="Lord of the ring 2",
                             description="Aventure")
        Movie.objects.create(title="Lord of the ring 3",
                             description="Aventure")
        Movie.objects.create(title="Fight club", description="Fight movie")
        self.review = Review.objects.create(grade=5, movie=self.movie)
        self.movie.actors.add(self.actor)

    def test_get_movies(self):
        """
        Ensure we can get movies list.
        """
        url = reverse('movie-list')
        response = self.client.get(url, format='json', page=2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 6)

    def test_get_movie(self):
        """
        Ensure we can get movie detail.
        """
        url = reverse('movie-detail', args=[self.movie.pk])
        response = self.client.get(url, format='json',)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.movie.title)
        self.assertEqual(response.data["description"], self.movie.description)
        self.assertEqual(response.data["actors"], [OrderedDict(
            [("id", self.actor.pk),
             ("first_name", self.actor.first_name),
             ("last_name", self.actor.last_name)])])
        self.assertEqual(response.data["reviews"], [OrderedDict(
            [("id", self.review.pk),
             ("grade", self.review.grade),
             ("movie", self.movie.pk)])])
