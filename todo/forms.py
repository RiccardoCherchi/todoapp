from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from todo.models import Todo


class FormRegistrazione(UserCreationForm):
    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FormTodo(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True),
    todo = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "insert a to-do"}), label="", required=True)
