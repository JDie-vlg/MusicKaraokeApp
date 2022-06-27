from django.contrib import admin
from .models import Musics, MusicGroup


# Register your models here.

@admin.register(Musics)
class MusicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'executor', 'song_name')


@admin.register(MusicGroup)
class MusicGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'list_name', 'get_musics')
