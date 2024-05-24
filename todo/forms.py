from .models import *
from django import forms
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = todo_data
        fields = "__all__"