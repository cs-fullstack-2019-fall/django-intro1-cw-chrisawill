from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index():
    return HttpResponse("This is a bad request")

def music(request):
    return  HttpResponse("Melanie Martinez(MM/), Buto(Buto/), Jonas Brothers(JB/)")

def MM():
    return HttpResponse("She wrote and directed her feature film, K-12")
def Buto():
    return HttpResponse("Has an absoLUTE banger titled 'Blessing'")
def JB():
    return HttpResponse("I went to one of their concerts. Best concert ive ever been to")