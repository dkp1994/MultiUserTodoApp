from django.forms import ModelForm
from .models import Todoapp


class TodoForm(ModelForm):
    class Meta:
        model = Todoapp
        fields = ['title','status','priority']