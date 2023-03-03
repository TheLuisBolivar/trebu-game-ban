from django.urls import path
from apps.blacklists.api.api import blacklist_api_view_get, blacklist_api_view_post

urlpatterns = [
    path('', blacklist_api_view_post, name='blacklist_post'),
    path('', blacklist_api_view_get, name='blacklist_get'),
]
