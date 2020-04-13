from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

#def home(request):
    #return HttpResponse('Hello there friend')

def home(request):
    return render(request, 'generator/home.html', {'password': 'tabur'})

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    #Uppercase option:
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    #Special Character option:
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-'))

    #Numbers option:
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))


    #length = 10 #This is fixed length. This will change as variable below
    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
