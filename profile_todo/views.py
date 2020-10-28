from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def landing_page(request):
    return render(request, 'profile_todo/base.html')


def home(request):
    return render(request, 'profile_todo/home.html')


def create(request):
    return HttpResponse(f'working')
