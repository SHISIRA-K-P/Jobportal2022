from django import forms
from employer.models import Jobs





# class JobForm(forms.Form):
#     job_title_name = forms.CharField()
#     company_name = forms.CharField()
#     location = forms.CharField()
#     salary = forms.IntegerField()
#     experience = forms.IntegerField()


    # OR



class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        fields="__all__"


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name",'last_name','email','username','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())