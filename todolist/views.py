from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.
@login_required(login_url='/todolist/login/')

# SHOW TODOLIST
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'list_task' : data_task,
        'username': request.user.username,
    }

    return render(request, "todolist.html", context)

# UPDATE STATUS
def update_status(request,id):
    task = Task.objects.get(id=id)
    task.is_finished = not task.is_finished
    task.save()

    return redirect('todolist:show_todolist')

# DELETE TASK
def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect('todolist:show_todolist')

# TAMBAH TASK
def create_task(request):
    task_form = TaskForm()

    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        task_form.instance.user = request.user
        if task_form.is_valid():
            task_form.save()
            messages.success(request, 'Task berhasil ditambahkan')
            return redirect('todolist:show_todolist')

    else:
        task_form = TaskForm()

    return render(request, 'create_task.html', {'form': task_form})

# REGISTER
def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# LOGIN
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# LOGOUT
def logout_user(request):
    logout(request)
    return redirect('todolist:login')