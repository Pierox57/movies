from rest_framework.test import APITestCase
from movies.models import Movie
from movies.serializers import MovieSerializer
from movies.models import Actor
from movies.serializers import ActorSerializer
from movies.models import Review
from movies.serializers import ReviewSerializer


class MovieSerializerTests(APITestCase):
    """
    Test movie serializer.
    """

    def setUp(self):
        """
        Needed data for running tests.
        """
        movie = Movie.objects.create(
            title="Kill Bill", description="Fight movie")
        self.movie_serializer = MovieSerializer(movie)

    def test_contain_expected_fields(self):
        """
        Ensure that serializer provide expected keys.
        """
        movie_serializer_data_keys = self.movie_serializer.data.keys()
        self.assertEqual(set(movie_serializer_data_keys), set(
            ["id", "title", "description", "actors", "reviews"]))


class ActorSerializerTests(APITestCase):
    """
    Test actor serializer.
    """

    def setUp(self):
        """
        Needed data for running tests.
        """
        actor = Actor.objects.create(first_name="Uma", last_name="Thurman")
        self.actor_serializer = ActorSerializer(actor)

    def test_contain_expected_fields(self):
        """
        Ensure that serializer provide expected keys.
        """
        actor_serializer_data_keys = self.actor_serializer.data.keys()
        self.assertEqual(set(actor_serializer_data_keys),
                         set(["id", "first_name", "last_name"]))


class ReviewSerializerTests(APITestCase):
    """
    Test review serializer.
    """

    def setUp(self):
        """
        Needed data for running tests.
        """
        movie = Movie.objects.create(
            title="Kill Bill", description="Fight movie")
        review = Review.objects.create(grade=5, movie=movie)
        self.review_serializer = ReviewSerializer(review)

    def test_contain_expected_fields(self):
        """
        Ensure that serializer provide expected keys.
        """
        review_serializer_data_keys = self.review_serializer.data.keys()
        self.assertEqual(set(review_serializer_data_keys),
                         set(["id", "grade", "movie"]))
