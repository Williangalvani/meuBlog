from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from models import FamilySearchDownload
# Create your views here.
from scripts import searcher
from forms import SearchForm



def viewDownload(request, name):
    instance = FamilySearchDownload.objects.filter(filename=name)[0]
    return render_to_response("results.html",
                              {"instance": instance},
                              context_instance=RequestContext(request))

def viewDownloadRaw(request, name):
    instance = FamilySearchDownload.objects.filter(filename=name)[0]
    return HttpResponse(instance.log)

def index(request):
    if request.method == 'POST':
        if FamilySearchDownload.objects.filter(filename=request.POST["filename"]).exists():
            instance = FamilySearchDownload.objects.filter(filename=request.POST["filename"])[0]
        else:
            instance = SearchForm(request.POST)
            if instance.is_valid():
                instance = instance.save()
                downloader = searcher.Downloader(instance)
                downloader.start()
            else:
                return render_to_response("search.html",
                                          {"form": SearchForm()},
                                          context_instance=RequestContext(request))
        return redirect("Results", name=instance.filename)
    else:
        form = SearchForm()
        return render_to_response("search.html",
                                  {"form": form},
                                  context_instance=RequestContext(request))
