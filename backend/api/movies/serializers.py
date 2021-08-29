from rest_framework import serializers
from movies.models import Movie
from movies.models import Actor
from movies.models import Review
from drf_writable_nested.serializers import WritableNestedModelSerializer


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


class MovieSerializer(WritableNestedModelSerializer):
    """
    Serializer class based on the movie model.
    """
    actors = ActorSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "actors", "reviews"]


"""class MovieUpdateSerializer(serializers.ModelSerializer):
    \"""
    Serializer class based on the movie model for updating.
    \"""
    actors = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Actor.objects.all())
    reviews = serializers.PrimaryKeyRelatedField(
        many=True, read_only=False, queryset=Review.objects.all())

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "actors", "reviews"]
"""
