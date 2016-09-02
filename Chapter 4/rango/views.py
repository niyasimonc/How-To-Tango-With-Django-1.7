# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: Hello world! ")
def about(request):
    return HttpResponse("Rango says: Hello world! <br/> hai <br/> second <br/> <a href='/rango/about'>About</a>")

