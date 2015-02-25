from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from models import Post
from django.template import RequestContext


def index(request):
    posts = Post.objects.order_by('-date')[:5]
    if not posts:
        empty = Post()
        empty.name = "No posts here!"
        posts = [empty]
    return render_to_response("index.html",
                              {"posts": posts},
                              context_instance=RequestContext(request))


def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render_to_response("post.html",
                              {"Post": post},
                              context_instance=RequestContext(request))

