from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from profile_todo.forms import ProfileForm, TodoForm
from profile_todo.models import Todo, Profile


def home(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'profile_todo/home.html', {'todos': todos})
        return render(request, 'profile_todo/home.html', {'todos': todos})
    form = ProfileForm()
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'profile_todo/home.html', context)


def create(request):
    context = {
        'form': TodoForm()
    }
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.prof = form.save()
            form.prof.save()

            return redirect('home')
        return render(request, 'profile_todo/create.html', context)

    return render(request, 'profile_todo/create.html', context)

def edit(request, pk):
    return None

def delete(request, pk):
    return None



