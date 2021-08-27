from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from movies.models import Movie


class MoviesViewsTests(APITestCase):
    """
    Test movies views.
    """

    def setUp(self):
        Movie.objects.create(title="Kill Bill", description="Fight movie")
        Movie.objects.create(title="Kill Bill 2", description="Fight movie")
        Movie.objects.create(title="Lord of the ring 1",
                             description="Aventure")
        Movie.objects.create(title="Lord of the ring 2",
                             description="Aventure")
        Movie.objects.create(title="Lord of the ring 3",
                             description="Aventure")
        Movie.objects.create(title="Fight club", description="Fight movie")

    def test_get_movies(self):
        """
        Ensure we can get movies list.
        """
        url = reverse('movie-list')
        response = self.client.get(url, format='json', page=2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 6)
