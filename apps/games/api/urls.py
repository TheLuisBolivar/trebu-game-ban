from django.urls import path
from apps.games.api.api import game_api_view_get, game_api_view_post

urlpatterns = [
    path('', game_api_view_post, name='game_post'),
    path('', game_api_view_get, name='game_get'),
]
