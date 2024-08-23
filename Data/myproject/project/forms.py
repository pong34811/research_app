from django import forms
from .models import Tag ,ProjectModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_select2.forms import 

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class TagForm (forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

# forms.py
class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ["project_name", "author_name", "project_date", "project_tag", "image", "pdf_file"]
        widgets = {
            'project_tag': forms.Select2MultipleWidget,
        }

