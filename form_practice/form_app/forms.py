from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from form_app.models import UserInfo

class UserForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput())

    class Meta():
        models = User


class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('profile_pic',)
