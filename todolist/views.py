""" lll """
from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodolistForm
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    """"  """
    todo_items = Todolist.objects.order_by('id')
    form = TodolistForm()
    context = {'todo_items': todo_items, 'forms':form}
    return render(request, 'todolist/index.html', context)

@require_POST   
def addTodoItem(request):
    """ """
    form = TodolistForm(request.POST)
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

