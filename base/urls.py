from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.romr, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/ ', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/ ', views.deleteRoom, name='delete-room'),
    path('test', views.test, name='test'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
]