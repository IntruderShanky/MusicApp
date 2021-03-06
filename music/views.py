from django.http import HttpResponse
from django.template import loader
from .models import Album
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import AlbumSerializer
from django.core.exceptions import ValidationError


class AlbumList(APIView):

    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = AlbumSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response = AlbumList.get(self, request).data
                response = {"success": True,
                            "artist": serializer.data["artist"],
                            "data": response}
                return Response(response)
        except ValidationError as e:
            return Response(e.message_dict(), status=400)
    
    def delete(self, request):
        if 'artist' in request.data.keys():
            d = request.data["artist"]
            Album.objects.filter(artist=d).delete()
            response = AlbumList.get(self, request).data
            response = {"success":True,
                        "data":response}
            return Response(response)
        data = {"success":False,
                "error":"artist key not found"}
        return Response(data, status=400)


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    data = {
        "all_albums": all_albums
    }
    return HttpResponse(template.render(data, request))


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Not Found")
    html = '<h1>' + album.album_title + '</h1><br><hr>'
    html += '<pre><b>Artist:</b> '+album.artist
    html += '<br><b>Genre:</b> ' + album.genre + '</pre>'
    return HttpResponse(html)
