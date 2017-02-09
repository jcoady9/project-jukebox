from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

from .models import Track, Album

# Create your views here.

def main_page(request):
    return render(request, 'jukebox/main.html', {})

class TrackIndexView(generic.ListView):
    template_name = 'jukebox/track_index.html'
    model = Track

    def get_queryset(self):
        return Track.objects.all()

class TrackView(generic.DetailView):
    template_name = 'jukebox/track_view.html'
    model = Track

class AlbumIndexView(generic.ListView):
    template_name = 'jukebox/album_index.html'
    model = Album

    def get_queryset(self):
        return Album.objects.all()

class AlbumView(generic.DetailView):
    template_name = 'jukebox/album_view.html'
    model = Album
