from django import forms
from .models import ResearchProject ,Event



class ResearchForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        fields = ["project_name","author_name","pdf_file"]
        


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_tag']


