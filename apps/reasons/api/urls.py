from django.urls import path
from apps.reasons.api.api import reason_api_view_get, reason_api_view_post

urlpatterns = [
    # path('', reason_api_view_post, name='reason_post'),
    path('', reason_api_view_get, name='reason_get'),
]
