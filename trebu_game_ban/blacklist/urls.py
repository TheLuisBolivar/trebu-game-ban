from django.urls import path
from . import views

urlpatterns = [
    path('', views.get, name='add_blacklist'),
    path('check/', views.post, name='get_blacklist_by_email')
]