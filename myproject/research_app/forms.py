from django import forms
from .models import ProjectModel, TagModel
from django_select2.forms import Select2MultipleWidget

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        fields = ['project_name', 'author_name', 'project_date', 'project_tag', 'image', 'pdf_file']
        widgets = {
            'project_tag': Select2MultipleWidget,
        }
