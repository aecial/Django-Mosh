from django.urls import path
from . import views
# Like Routes in Express
# URLConf
# always end with forward slash
urlpatterns = [
    path('hello/', views.say_hello)
]