from rest_framework.test import APITestCase
from movies.models import Movie
from movies.models import Actor
from movies.models import Review


class MovieModelTests(APITestCase):
    """
    Test movie model.
    """

    def setUp(self):
        """
        Needed data for running tests.
        """
        self.movie = Movie.objects.create(
            title="Kill Bill", description="Fight movie")

    def test_string_representation(self):
        """
        Ensure that model string representation is the title.
        """
        self.assertEqual(str(self.movie), "Kill Bill")


class ActorModelTests(APITestCase):
    """
    Test actor model.
    """

    def setUp(self):
        """
        Needed data for running tests.
        """
        self.actor = Actor.objects.create(
            first_name="Uma", last_name="Thurman")

    def test_string_representation(self):
        """
        Ensure that model string representation is first_name space last_name.
        """
        self.assertEqual(str(self.actor), "Uma Thurman")


class ReviewModelTests(APITestCase):
    """
    Test review model.
    """

    def setUp(self):
        """
        Needed data for running tests.
        """
        movie = Movie.objects.create(
            title="Kill Bill", description="Fight movie")
        self.review = Review.objects.create(grade=5, movie=movie)

    def test_string_representation(self):
        """
        Ensure that model string representation is movie's title : grade.
        """
        self.assertEqual(str(self.review), "Kill Bill : 5")
