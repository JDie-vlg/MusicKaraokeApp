from django.urls import path
from .views import API, MusicsList, MusicsDetail, MusicGroupList, MusicGroupDetail, \
    MusicApiView, MusicGroupApiView, DeletingApi

urlpatterns = [
    path('api/', API, name="API"),
    path('api/musics/', MusicApiView.as_view({'get': 'list',
                                              'post': 'create',
                                              'delete': 'destroy'}), name='music_api'),
    path('api/musics/<int:pk>/', MusicApiView.as_view({'get': 'retrieve',
                                                       'delete': 'destroy',
                                                       'put': 'update',
                                                       'post': 'create'}), name='music_detail_api'),
    path('api/deleting_music', DeletingApi.as_view(), name='deleting_music'),
    path('api/music_group/', MusicGroupApiView.as_view({'get': 'list',
                                                        'post': 'create'}), name='music_group_api'),
    path('api/music_group/<int:pk>/', MusicGroupApiView.as_view({'get': 'retrieve',
                                                                 'delete': 'destroy',
                                                                 'put': 'update',
                                                                 'post': 'create'}), name='music_group_detail_api'),
    path('music', MusicsList.as_view(), name="music_list"),
    path('music/<slug:slug>/', MusicsDetail.as_view(), name="music_detail"),
    path('music_group', MusicGroupList.as_view(), name="music_group_list"),
    path('music_group/<slug:slug>/', MusicGroupDetail.as_view(), name="music_group_detail"),
]
