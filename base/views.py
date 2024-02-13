from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Room
from .forms import RoomForm
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

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)