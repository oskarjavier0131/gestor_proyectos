from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateProject


def index(request):
    title = 'Bienvenido a la selva!!!!'
    return render(request, 'index.html', {'title': title})


def about(request):
    username = 'Lubianka'
    return render(request, 'about.html', {'username': username})


def hello(request, usser_id):
    return HttpResponse("<h2>Hola %s</h2>" % usser_id)


def projects(request):
    projects = Project.objects.all()
    # projects = list(Project.objects.values())
    return render(request, 'projects/projects.html', {'projects': projects})


def task(request):
    tasks = Task.objects.all()
    return render(request, 'task/task.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'GET':
        return render(request, 'task/create_task.html', {'form': CreateNewTask})
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            project_id=1)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateProject})
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
