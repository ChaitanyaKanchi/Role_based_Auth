from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'employee':
                return redirect('employee_dashboard')
            elif user.role == 'client':
                return redirect('client_dashboard')
    return render(request, 'accounts/login.html')

@login_required
def employee_dashboard(request):
    return render(request, 'accounts/employee_dashboard.html')

@login_required
def client_dashboard(request):
    return render(request, 'accounts/client_dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')