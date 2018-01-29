from django import forms
from django.contrib.auth.models import User
from .models import UserProfile,UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=("school","company","profession","address","aboutme","photo")

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("email",)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=("phone","birth")

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:
        model = User #内部类，声明本表单类应用的数据模型
        fields=("username","email")

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
           raise forms.ValidationError("passwords do not match.")
        return cd['password2']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)