# accounts/views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

# import Data Model
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('admin_list')  # Redirect ถ้าเป็น staff
            else:
                return redirect('user_list')   # Redirect ถ้าไม่เป็น staff
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


# admin/views.py
def admin_list(request):
    admin = request.user
    users_count = User.objects.count()
    return render (request, 'admins/admin_list.html',{'admin':admin ,'users_count':users_count})

def research_list(request):
    admin = request.user
    return render (request, 'admins/research_crud/research_list.html',{'admin':admin})


def user_list(request):
    return render (request, 'users/user_list.html')

