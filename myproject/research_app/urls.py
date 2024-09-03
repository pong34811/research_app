from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password, name='password_change'),
    
    path('dashboard/', views.admin_list, name='admin_list'),
    path('Research/', views.research_list, name='research_list'),
    path('Tag/', views.tag_list, name='tag_list'),

    path('research/add/', views.research_add, name='research_add'),
    path('research/edit/<int:id>/', views.research_edit, name='research_edit'),
    path('research/delete/<int:id>/', views.research_delete, name='research_delete'),
    
    path('tag/add/', views.tag_add, name='tag_add'),
    path('tag/edit/<int:id>/', views.tag_edit, name='tag_edit'),
    path('tag/delete/<int:id>/',views.tag_delete, name='tag_delete'),
    
    path('', views.user_list, name='user_list'),
]
