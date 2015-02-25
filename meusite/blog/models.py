from django.db import models

class Poster(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, null=True)
    body = models.TextField()
    author = models.ForeignKey(Poster)
    date = models.DateTimeField()

    def __init__(self, title, body, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.body = body
        self.title = title
