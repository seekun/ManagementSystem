from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, TestModel
from django import forms
from jsonfield import JSONField
from prettyjson import PrettyJSONWidget
import json
from splitjson.widgets import SplitJSONWidget


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
        fields = (
            'user_number', 'chinese_name', 'department', 'password', 'english_name', 'english_name2', 'english_name3',
            'english_name4')


#     def clean_jsonfield(self):
#         jdata = self.cleaned_data['jsonfield']
#         try:
#             json_data = json.loads(jdata)  # loads string as json
#             # validate json_data
#         except:
#             raise forms.ValidationError("Invalid data in jsonfield")
#         # if json data not valid:
#         # raise forms.ValidationError("Invalid data in jsonfield")
#         return jdata
#
#
# class testForm(forms.Form):
#     attrs = {'class': 'special', 'size': '40'}
#     data = forms.CharField(widget=SplitJSONWidget(attrs=attrs, debug=True))


class JsonForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'
        widgets = {
            'myjsonfield': PrettyJSONWidget(),
        }
