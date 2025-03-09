from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def hello_django(request):
    return HttpResponse("Hello, Django")


def get_all_tasks(request):
    # tasks = list(Task.objects.values())
    # return JsonResponse(tasks, safe=False)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_all_tasks')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('get_all_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'create_task.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    message = ""
    if request.method == 'POST':
        try:
            task.delete()
            message = "Task deleted successfully!"
        except Exception as e:
            message = "Task deletion failed!"
    else:
        message = "Invalid request."

    return render(request, 'delete_confirmation.html', {'message': message})
