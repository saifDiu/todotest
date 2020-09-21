from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .models import *

def index(request):
    tasks = task.objects.all()
    forms = Taskform()
    if request.method == 'POST':
        forms = Taskform(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/')

    context = {'tasks':tasks, 'forms':forms}

    return render(request, 'tasks/index.html', context)

def updateTask(request, pk):
    tasks = task.objects.get(id=pk)
    forms = Taskform(instance=tasks)
    if request.method == 'POST':
        forms = Taskform(request.POST, instance=tasks)
        if forms.is_valid():
            forms.save()
            messages.success(request, f'Task has been updated !')
            return redirect('index')
    context = {'forms':forms, 'task':tasks}

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    tasks = task.objects.get(id=pk)
    if request.method == 'POST':
        forms = Taskform(request.POST)
        tasks.delete()
        messages.success(request, f'Task has been Deleted !')
        return redirect('index')

    context = {'task':tasks}

    return render(request, 'tasks/delete_task.html', context)
