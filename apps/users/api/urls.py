from django.urls import path
from apps.users.api.api import user_api_view_post, user_api_view_get

urlpatterns = [
    path('', user_api_view_post, name='user_post'),
    path('', user_api_view_get, name='user_get'),
]
