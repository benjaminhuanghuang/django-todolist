# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import Todo
# Create your views here.


def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos': todos
    }
    # return HttpResponse('Hello')
    return render(request, 'index.html', context)

def details(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    context = {
        'todo': todo
    }
    # return HttpResponse('Hello')
    return render(request, 'detail.html', context)

def add(request):
    if (request.method == "POST"):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title = title, text = text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')