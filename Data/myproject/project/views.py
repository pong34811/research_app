from django.shortcuts import render, redirect, get_object_or_404
from .models import ProjectModel
from .forms import ProjectModelForm, SignupForm, LoginForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages

def signup_user(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user_authenticated = authenticate(
                username=signup_form.cleaned_data['username'],
                password=signup_form.cleaned_data['password1']
            )
            if user_authenticated is not None:
                auth_login(request, user_authenticated)
                return redirect('project_list')
    else:
        signup_form = SignupForm()
    return render(request, 'users/signup.html', {'form': signup_form})

def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            auth_login(request, user)
            return redirect('project_list')
    else:
        login_form = LoginForm()
    return render(request, 'users/login.html', {'form': login_form})

def logout_user(request):
    auth_logout(request)
    return redirect('login')


@login_required
def list_projects(request):
    query = request.GET.get('q', '')
    projects = ProjectModel.objects.all()
    projects_count = projects.count()  # Count of projects
    users_count = User.objects.count()  # Count of users
    
    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'query': query,
        'projects_count': projects_count,
        'users_count': users_count,
    })
@login_required
def add_project(request):
    if request.method == 'POST':
        project_form = ProjectModelForm(request.POST, request.FILES)
        if project_form.is_valid():
            new_project = project_form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            project_form.save_m2m()
            
            messages.success(request, "Successfully")
            
            return redirect('project_list')
    else:
        project_form = ProjectModelForm()
    return render(request, 'projects/project_add.html', {'form': project_form})

@login_required
def edit_project(request, id):
    project = get_object_or_404(ProjectModel, id=id, user=request.user)
    
    if request.method == 'POST':
        project_form = ProjectModelForm(request.POST, request.FILES, instance=project)
        if project_form.is_valid():
            project_form.save()
            
            messages.success(request, "Successfully EDIT")
            return redirect('project_list')
    else:
        project_form = ProjectModelForm(instance=project)

    return render(request, 'projects/project_edit.html', {'form': project_form, 'project': project})

@login_required
def delete_project(request, id):
    project = get_object_or_404(ProjectModel, id=id, user=request.user)

    if request.method == 'POST':
        project.delete()
        
        messages.success(request, "Successfully DELETE")
        return redirect('project_list')

    return render(request, 'projects/delete_modal.html', {'project': project})
