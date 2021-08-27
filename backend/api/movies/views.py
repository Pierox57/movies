from rest_framework import mixins
from movies.serializers import MovieSerializer
from movies.models import Movie
from rest_framework import viewsets


class MovieViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides list actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
