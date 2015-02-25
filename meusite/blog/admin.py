from django.contrib import admin
from models import Post, Poster
from forms import PostForm
from pagedown.widgets import AdminPagedownWidget
from django.db import models as dbmodels



class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Post, PostAdmin)

admin.site.register(Poster)

