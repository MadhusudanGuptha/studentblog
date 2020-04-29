from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm






class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Reg No', max_length=10)
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


