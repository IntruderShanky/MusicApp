from django.http import HttpResponse
from .models import Album


def index(request):
    html = '<h1>All Albums</h1><hr>'
    for album in Album.objects.all():
        url = "/music/" + str(album.id)
        html += '<a href="'+str(url)+'">' + album.album_title + '</a><br>'

    return HttpResponse(html)


def detail(request, album_id):
    album = Album.objects.get(id=album_id)
    html = '<h1>' + album.album_title + '</h1><br><hr>'
    html += '<pre><b>Artist:</b> '+album.artist
    html += '<br><b>Genre:</b> ' + album.genre + '</pre>'
    return HttpResponse(html)
