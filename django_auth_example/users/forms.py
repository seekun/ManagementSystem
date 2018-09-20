from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", 'email')


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'user_number', 'chinese_name', 'department', 'password', 'english_name', 'english_name2', 'english_name3',
            'english_name4')
