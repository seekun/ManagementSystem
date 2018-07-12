from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", 'email')


# class Change(User):
#
# class UserForm(forms.Form):
#     user_number = forms.CharField()
#     chinese_name = forms.CharField()
#     english_name = forms.CharField()
#     # list字段,可以有多个english_name
#     department = forms.CharField()
class UserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('user_number', 'chinese_name', 'english_name', 'department',  'password')

