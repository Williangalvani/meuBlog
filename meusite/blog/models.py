from django.db import models

class Poster(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(Poster)
    date = models.DateTimeField()

