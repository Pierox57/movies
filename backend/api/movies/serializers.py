from rest_framework import serializers
from movies.models import Movie
from movies.models import Actor
from movies.models import Review


class ActorSerializer(serializers.ModelSerializer):
    """
    Serializer class based on the actor model.
    """

    class Meta:
        model = Actor
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer class based on the review model.
    """

    class Meta:
        model = Review
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer class based on the movie model.
    """
    actors = ActorSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "actors", "reviews"]
