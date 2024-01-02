from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def home(request):
  todos = Todo.objects.all()
  content = {'todos':todos}
  return render(request,'index.html', context = content)

def create(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')
    status = request.POST.get('status')
    Todo.objects.create(name=name,description = description, status=status)
    return redirect('home')
  content= {'mode':'create'}
  return render(request, 'create.html',context=content)

def edit(request,pk):
  todo= Todo.objects.get(id=pk)
  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')
    status = request.POST.get('status')
    todo.name = name
    todo.description = description
    todo.status = status
    todo.save()
    return redirect('home')
  print(todo)
  content={'mode':'edit','todo':todo}
  return render(request,'create.html',context=content)

def delete(request,pk):
  todo = Todo.objects.get(id=pk)
  todo.delete()
  return redirect('home')

def deleteall(request):
  todo = Todo.objects.all()
  todo.delete()
  return redirect('home')

