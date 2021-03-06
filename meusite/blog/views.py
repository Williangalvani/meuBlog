from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from models import Post
from django.template import RequestContext


def index(request):
    posts = Post.objects.filter(published=True).order_by('-date')
    if not posts:
        empty = Post()
        empty.name = "No posts here!"
        posts = [empty]
    return render_to_response("index.html",
                              {"posts": posts},
                              context_instance=RequestContext(request))

def view_post(request, post_id, title):
    post = get_object_or_404(Post, id=post_id)
    return render_to_response("post.html",
                              {"post": post},
                              context_instance=RequestContext(request))

def view_redirect(request):
    return redirect("/blog/")

def apps_index(request):
    return render_to_response("apps_index.html",
                              context_instance=RequestContext(request))