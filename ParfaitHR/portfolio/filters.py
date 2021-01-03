import django_filters
from django import forms
from .models import Job

class JobFilter(django_filters.FilterSet):
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