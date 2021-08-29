from rest_framework import mixins
from movies.serializers import MovieSerializer
from movies.serializers import ActorSerializer
from movies.serializers import ReviewSerializer
from movies.models import Movie
from movies.models import Actor
from movies.models import Review
from rest_framework import viewsets


class MovieViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset that provides list, retrieve, update actions on movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ActorViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    A viewset that provides list action on actor.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = None


class ReviewViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
    A viewset that provides create action on review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = None
