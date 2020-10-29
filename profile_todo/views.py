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

        context = {
            'todos': todos,
            'form': ProfileForm(request.POST)
        }
        return render(request, 'profile_todo/home.html', context)
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
        context = {
            'form': TodoForm(request.POST)
        }
        return render(request, 'profile_todo/create.html', context)

    return render(request, 'profile_todo/create.html', context)


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.prof = form.save()
            form.prof.save()
            return redirect('home')
        return render(request, 'profile_todo/edit.html', {'form': form})
    return render(request, 'profile_todo/edit.html', {'form': form})


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'profile_todo/delete.html', {'todo': todo})


def details(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'profile_todo/details.html', {'todo': todo})
