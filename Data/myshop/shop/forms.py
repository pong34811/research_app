from django import forms
from .models import Shop, Tag
from django_select2.forms import Select2MultipleWidget

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'tags']
        widgets = {
            'tags': Select2MultipleWidget,
        }
