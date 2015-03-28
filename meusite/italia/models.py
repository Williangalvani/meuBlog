from django.db import models

# Create your models here.


class FamilySearchDownload(models.Model):
    log = models.TextField(blank=True, null=True,default="")
    url = models.CharField(max_length=200)
    filename = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
