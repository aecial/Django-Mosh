from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import Room, Category, Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# rooms =[
#     {'id':1, 'name': 'Lets learn Python'},
#     {'id':2, 'name': 'Lets learn Java'},
#     {'id':3, 'name': 'Lets learn C#'},
# ]
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Does not Exist!')
    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')
def say_hello(request):
    return JsonResponse({'message': 'I am Ted'})
def romr(request):
    # ORM To get all
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # topic__name__icontains = not case sensitive and returns if a value in q matches with the letters
    # in the topic; topic__name_contains = case sesitive
    # search room if a character is contained in topic or in name or in description
    # using the Q Lookup Method
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)) 
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
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

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        # pass the instance to update only
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

def test(request):
    category = Category.objects.all
    context  = {'category': category}
    return render(request, 'base/testPage.html', context)