from django.shortcuts import render
from .models import Task  

def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        ins=Task(title=title, desc=desc)
        ins.save()
        context = {'success': True}

    return render(request, 'index.html',context)

def task(request):
    alltasks = Task.objects.all()
    print(alltasks)
    context = {'tasks': alltasks}  
    return render(request, 'task.html', context)