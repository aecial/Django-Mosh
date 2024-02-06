from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Views are like endpoint functions
def say_hello(request):
    # can return html element
    
    return HttpResponse('<h1>Hello World </h1>')