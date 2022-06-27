from rest_framework import serializers
from .models import Musics, MusicGroup


class MusicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musics
        fields = "__all__"


class MusicGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicGroup
        fields = "__all__"
