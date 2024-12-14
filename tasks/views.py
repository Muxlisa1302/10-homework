from django.shortcuts import render, get_object_or_404, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'tasks/list.html', ctx)

def task_create(request):
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        if task_title and description and due_date:
            Task.objects.create(
                task_title=task_title,
                description=description,
                due_date=due_date
            )
            return redirect('tasks:list')
    return render(request,'tasks/form.html')


def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    ctx = {'task': task}
    return render(request, 'tasks/detail.html', ctx)


