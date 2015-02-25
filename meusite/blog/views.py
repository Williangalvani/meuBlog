from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from models import Post
from django.template import RequestContext


def index(request):
    posts = Post.objects.order_by('-date')[:5]
    if not posts:
        posts= [Post("No posts here!", "")]
    return render_to_response("index.html",
                              {"posts": posts},
                              context_instance=RequestContext(request))