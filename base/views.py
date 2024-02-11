from django.shortcuts import render
from django.http import JsonResponse
from .models import Room
# Create your views here.
# rooms =[
#     {'id':1, 'name': 'Lets learn Python'},
#     {'id':2, 'name': 'Lets learn Java'},
#     {'id':3, 'name': 'Lets learn C#'},
# ]
def say_hello(request):
    return JsonResponse({'message': 'I am Ted'})
def romr(request):
    # ORM To get all
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
#pk for dynamic route
def room(request, pk):
    # Check for the room number
    rooms = Room.objects.get(id=pk)
    context = {'information': rooms}   
    return render(request, 'base/room.html', context)