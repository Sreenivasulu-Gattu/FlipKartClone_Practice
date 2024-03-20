from django.shortcuts import render

# Create your views here.

from app.forms import *

def home(request):
    return render(request,'home.html')


def user_signup(request):
    ufo = UserForm()
    d = {'ufo':ufo}
    return render(request,'user_signup.html',d)
