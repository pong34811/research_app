# accounts/views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

# import Data Model
from django.contrib.auth.models import User
from .models import ProjectModel, TagModel

#forms.py
from .forms import ProjectForm  # สมมุติว่าคุณมีฟอร์มสำหรับโปรเจคนี้

# messages
from django.contrib import messages

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
    projects = ProjectModel.objects.all()
    tags = TagModel.objects.all() 
    admin = request.user
    return render (request, 'admins/research_crud/research_list.html',{'admin':admin,'projects':projects,'tags':tags})

@login_required
def research_add(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        author_name = request.POST.get('author_name')
        project_date = request.POST.get('project_date')
        tag_ids = request.POST.getlist('project_tag')  # รับค่าแท็กจากฟอร์ม
        image = request.FILES.get('image')  # รับไฟล์รูปภาพจากฟอร์ม
        pdf_file = request.FILES.get('pdf_file')  # รับไฟล์ PDF จากฟอร์ม

        # ดึงข้อมูลแท็กจากฐานข้อมูลตาม ID
        tags = TagModel.objects.filter(id__in=tag_ids)

        # สร้าง instance ของ ProjectModel
        project = ProjectModel.objects.create(
            user=request.user,  # กำหนด user ที่เป็นผู้เพิ่ม project นี้
            project_name=project_name,
            author_name=author_name,
            project_date=project_date,
            image=image,
            pdf_file=pdf_file
        )
        
        # กำหนดแท็กที่เลือกไว้ให้กับ project
        project.project_tag.set(tags)
        
        # บันทึกข้อมูล project
        project.save()

        return redirect('research_list')  # เปลี่ยนเส้นทางไปยังรายการ project

    # ดึงข้อมูลแท็กทั้งหมดเพื่อส่งไปยังเทมเพลต
    tags = TagModel.objects.all()
    return render(request, 'admins/research_crud/research_add_modal.html', {'tags': tags})

def user_list(request):
    return render(request, 'users/user_list.html')

