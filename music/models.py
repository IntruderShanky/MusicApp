from django.db import models


class Album(models.Model):
    artists = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    album_title = models.CharField(max_length=500)
    album_logo = models.CharField(max_length=1000)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)

