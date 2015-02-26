from django.db import models

class Poster(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "{0} ({1})".format(self.name, self.email)


class Post(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(Poster)
    date = models.DateTimeField()
    image = models.ImageField(null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return '"{0}" by {1} at {2}'.format(self.title, self.author.name, self.date.strftime('%B, %d %Y'))
