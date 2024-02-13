from django.urls import path
from . import views
urlpatterns = [
    path('', views.romr, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room')
]