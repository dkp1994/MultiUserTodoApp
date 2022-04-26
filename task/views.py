from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login as loginuser , logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import TodoForm
from .models import Todoapp
from django.contrib.auth.decorators import login_required

# use decorators for checking the user is login or ont
@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm()
        todos = Todoapp.objects.filter(user=user)
        return render(request,'task/index.html', {'form': form,'todos': todos})
    # else:
    #     return render(request,'task/index.html')

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request,'task/login.html',{'form':form})
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                loginuser(request,user)
                return redirect('index')
        else:
            return render(request,'task/login.html',{'form':form})


def signin(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request,'task/signin.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm(request.POST)
            return render(request,'task/signin.html', {'form': form})


def userlogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('index')
        else:
            return render(request,'task/index.html', {'form': form})


def delete_todo(request,id):
    Todoapp.objects.get(id=id).delete()
    return redirect('index')

def change_todo(request,id,status):
    todo = Todoapp.objects.get(id=id)
    todo.status = status
    todo.save()
    return redirect('index')
    