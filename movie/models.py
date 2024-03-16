from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=1, choices=[(i, i * '*') for i in range(1, 6)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
