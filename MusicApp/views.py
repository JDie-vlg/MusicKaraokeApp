from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from rest_framework.decorators import action

from .models import Musics, MusicGroup
from .modelserializers import MusicsSerializer, MusicGroupSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.

def API(request):
    return HttpResponse("API is working fine")


class MusicsList(ListView):
    model = Musics
    template_name = "music/musics_list.html"
    queryset = Musics.objects.all()


class MusicsDetail(DetailView):
    model = Musics
    template_name = "music/musics_detail.html"
    slug_field = 'executor'


class MusicGroupList(ListView):
    model = MusicGroup
    template_name = "music_group/music_group_list.html"
    queryset = MusicGroup.objects.all()


class MusicGroupDetail(DetailView):
    model = MusicGroup
    template_name = "music_group/music_group_detail.html"
    slug_field = 'list_name'


class MusicApiView(viewsets.ModelViewSet):
    queryset = Musics.objects.all()
    serializer_class = MusicsSerializer


class MusicGroupApiView(viewsets.ModelViewSet):
    queryset = MusicGroup.objects.all()
    serializer_class = MusicGroupSerializer

