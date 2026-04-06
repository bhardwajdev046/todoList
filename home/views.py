from django.shortcuts import render
from .models import Task  

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title:
            Task.objects.create(title=title, desc=desc)
    return render(request, 'index.html', {'tasks': Task.objects.all()})


def task(request):
    return render(request, 'task.html')