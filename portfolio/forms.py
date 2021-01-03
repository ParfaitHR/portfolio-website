from django.forms import ModelForm, Form
from django import forms
from django.contrib.auth.forms import UserCreationForm     
from django.contrib.auth.models import User 

from .models import Job

class ContactForm(Form):
    InputFullName = forms.CharField(
        label='Full Name', 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
        )
    InputEmail = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    InputNumber = forms.CharField(
        label='Contact Number',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    InputQuery = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
        )

class CVForm(Form):
    InputName = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    InputEmail = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    InputNumber = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    InputCV = forms.FileField()

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['job_title','company_name','salary','vacancies','status']

        widgets = {
            'job_title' : forms.TextInput(attrs={'class':'form-control'}),
            'company_name' : forms.TextInput(attrs={'class':'form-control'}),
            'salary' : forms.NumberInput(attrs={'class':'form-control'}),
            'vacancies' : forms.NumberInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'}),

        }
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Username', 'required':'True', 'autofocus':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Email Address', 'required':'True'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password', 'required':'True'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password', 'required':'True'}),
            }