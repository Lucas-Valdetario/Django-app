from django import forms
from .models import AppModel

class tarefaForm(forms.ModelForm):
    class Meta:
        model = AppModel
        fields = ['name', 'description', 'complete']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }