from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ("artist", "genre", "album_title")
        # fields = '__all__'

