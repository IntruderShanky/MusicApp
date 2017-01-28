from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    data = {
        "all_albums": all_albums
    }
    return HttpResponse(template.render(data, request))


def detail(request, album_id):
    album = Album.objects.get(id=album_id)
    html = '<h1>' + album.album_title + '</h1><br><hr>'
    html += '<pre><b>Artist:</b> '+album.artist
    html += '<br><b>Genre:</b> ' + album.genre + '</pre>'
    return HttpResponse(html)
