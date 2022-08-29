from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Todo, StatusChoice

def index(request):
    tasks = Todo.objects.all()
    return render(request, "base.html", {"tasks": tasks})


@require_http_methods(['POST'])
def add_task(request):
    todo = None
    title = request.POST.get('task',None)
    print(request.POST.__dict__)
    if title:
        todo = Todo.objects.create(task=title)
    return render(request, 'todos/snippets/task.html', {"task": todo})


@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.status = StatusChoice.Complete
    todo.save()
    return render(request, 'todos/snippets/task.html', {"task": todo})

@require_http_methods(['DELETE'])
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponse()
