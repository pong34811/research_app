from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('dashboard/', views.admin_list, name='admin_list'),
    path('Research/', views.research_list, name='research_list'),

    path('research/add/', views.research_add, name='research_add'),
    path('research/edit/<int:id>/', views.research_edit, name='research_edit'),
    path('research/delete/<int:id>/', views.research_delete, name='research_delete'),
    
    path('home/', views.user_list, name='user_list'),
]
