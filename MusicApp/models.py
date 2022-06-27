from django.db import models
from django.urls import reverse


class Musics(models.Model):
    executor = models.CharField('Исполнитель', max_length=60, blank=False, null=False)
    song_name = models.CharField('Название песни', max_length=60, blank=False, null=False)
    song_image = models.ImageField('Изображение группы', blank=False, null=False)

    def __str__(self):
        return f'{self.executor} - {self.song_name}'

    def get_absolute_url(self):
        return reverse('music_detail', kwargs={'slug': self.executor})


class MusicGroup(models.Model):
    list_name = models.CharField('Название плейлиста', max_length=60, blank=False, null=False)
    music = models.ManyToManyField(Musics)

    def __str__(self):
        return self.list_name

    def get_musics(self):
        return ", ".join([m.executor for m in self.music.all()])

    def get_absolute_url(self):
        return reverse('music_group_detail', kwargs={'slug': self.list_name})

