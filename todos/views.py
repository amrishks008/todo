from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def list_todo_items(request):
    todo_items = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todo_list': todo_items})


def insert_todo_item(request):
    content = request.POST['content']
    todo = Todo(content=content)
    todo.save()
    return redirect('/todos/list/')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')
