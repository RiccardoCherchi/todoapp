from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from todo.models import Todo
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import FormRegistrazione, FormTodo

# Create your views here.


def todoView(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
        if request.method == "POST":
            form = FormTodo(request.POST)
            if form.is_valid():
                Todo.objects.create(user=request.user, todo=form.cleaned_data["todo"])
                return HttpResponseRedirect('/')
        else:
            form = FormTodo()
            context = {"form": form, "todos": todos}
            return render(request, 'todo.html', context)
    else:
        return HttpResponseRedirect('/login')


def deleteTodo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.user == request.user:
        Todo.delete(todo)
        messages.success(request, "to do delete successfully")
        return HttpResponseRedirect('/')
    else:
        messages.error(request, "you are not authorized to delete this to do")
        return HttpResponseRedirect('/')


def registrazioneView(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = FormRegistrazione()
    context = {'form': form}
    return render(request, 'registrazione.html', context)
