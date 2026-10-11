from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Task

# Create your views here.
def task_list(request):
    data = Task.objects.all()
    HttpResponse(data)
    return render(request, 'task/task_list.html', {'tasks': data})

def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()   
        description = request.POST.get('description', '').strip()
        if title:   
            Task.objects.create(title=title, description=description)       
            return redirect(reverse('task_list'))
        error = 'Title can not be empty'
        return render(request, 'task/task_add.html', {'error': error, 'title': title, 'description': description})
    return render(request, 'task/task_form.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        if request.POST.get('title', '').strip():
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.completed = request.POST.get('completed') == 'on'
            task.save()
            return redirect(reverse('task_list'))  
        else:
            error = 'Title can not be empty'
            return render(request, 'task/task_form.html', {'task': task, 'error': error})
    return render(request, 'task/task_form.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task:
        task.delete()
        return redirect(reverse('task_list'))
    return render(request, 'task/task_delete.html', {'task': task})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect(reverse('task_list'))