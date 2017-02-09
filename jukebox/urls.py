from django.conf.urls import url

from . import views

app_name = 'jukebox'
urlpatterns = [
    url(r'^albums/$', views.AlbumIndexView.as_view(),name='album_index'),
    url(r'^tracks/$', views.TrackIndexView.as_view(), name='track_index'),
    url(r'^(?P<pk>[0-9]+)/tracks/$', views.TrackView.as_view(),name='track_detail'),
    url(r'^(?P<pk>[0-9]+)/ablums/$', views.AlbumView.as_view(),name='album_detail'),
    url(r'^$', views.main_page,name='main'),
]
