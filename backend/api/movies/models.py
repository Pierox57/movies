from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Actor(models.Model):
    """
    Actor model class.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        """
        String representation.
        """
        return self.first_name + " " + self.last_name


class Movie(models.Model):
    """
    Movie model class
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(
        Actor, related_name="movies")

    class Meta:
        ordering = ['title']

    def __str__(self):
        """
        String representation.
        """
        return self.title


class Review(models.Model):
    """
    Review model class
    """
    grade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(
        Movie, related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation.
        """
        return self.movie.title + " : " + str(self.grade)
