from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_projects, name='project_list'),
    path('add/', views.add_project, name='add_project'),
    path('edit/<int:id>/', views.edit_project, name='edit_project'),
    path('delete/<int:id>/', views.delete_project, name='delete_project'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
