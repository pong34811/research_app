from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('dashboard/', views.admin_list, name='admin_list'),
    path('Research', views.research_list, name='research_list'),
  
    
    path('Home/', views.user_list, name='user_list'),

]