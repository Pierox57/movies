from rest_framework import mixins
from movies.serializers import MovieSerializer
from movies.serializers import ActorSerializer
from movies.models import Movie
from movies.models import Actor
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
