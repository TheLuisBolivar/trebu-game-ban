from django.urls import path
from . import views

urlpatterns = [
    path('', views.postBlacklist, name='add_blacklist'),
    path('check/<str:email>', views.getInfoBlackList, name='get_blacklist_by_email'),
    path('game/', views.create_game, name='create_game')
]