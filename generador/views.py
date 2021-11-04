import random
from typing import List
from django.shortcuts import render
from django.http import HttpResponse 
import random


# Create your views here.

def about(request):
    return render(request,'generador/about.html')

def home(request):
    return render(request,'generador/home.html')

def password(request):

    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))#Obtiene la longitud de caracteres

    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('especial'):
        caracteres.extend(list('!#$@%&?¿*+_-<>()¡'))

    if request.GET.get('number'):
        caracteres.extend(list('1234567890'))



    for x in range(length):
        generated_password += random.choice(caracteres)
    

    return render(request,'generador/password.html',{'password': generated_password})
