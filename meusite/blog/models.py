from django.db import models

# Create your models here.


class Poster(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(Poster)
    date = models.DateTimeField()