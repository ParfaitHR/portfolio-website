import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives  
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Job
from .forms import ContactForm, CVForm, JobForm, CreateUserForm
from .filters import JobFilter
from .decorators import *

def home(request):
    jobs = Job.objects.order_by('salary')[:4]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Query - ' + form.cleaned_data['InputFullName']
            email = form.cleaned_data['InputEmail']
            content = 'Hi Startup, \n' + form.cleaned_data['InputQuery'] + '\nRegards\n' + form.cleaned_data['InputFullName'] + '\n' + form.cleaned_data['InputNumber']

            send_mail(
                subject,
                content,
                email,
                ['parfaithrm@gmail.com']
            )

            content = {
                'form': form,
                'jobs': jobs,
                'title' : 'Home',
                'css' : 'css/home.css',
                'message':'Your Query has been sent successfully\nWe will get back to you as soon as possible',
            }

            return render(request, 'portfolio/home.html', content) 
    else:
            form = ContactForm()

    content = {
        'form': form,
        'jobs': jobs,
        'title' : 'Home',
        'css' : 'css/home.css',
    }

    return render(request, 'portfolio/home.html', content)

def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Query - ' + form.cleaned_data['InputFullName']
            email = form.cleaned_data['InputEmail']
            content = 'Hi Startup, \n' + form.cleaned_data['InputQuery'] + '\nRegards\n' + form.cleaned_data['InputFullName'] + '\n' + form.cleaned_data['InputNumber']

            send_mail(
                subject,
                content,
                email,
                ['parfaithrm@gmail.com']
            )

            content = {
                'form': form,
                'title' : 'About',
                'css' : 'css/about.css',
                'message':'Query sent successfully',
            }

            return render(request, 'portfolio/about.html', content) 
    else:
            form = ContactForm()

    content = {
        'form': form,
        'title' : 'About',
        'css' : 'css/about.css',
    }

    return render(request, 'portfolio/about.html', content)

def services(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Query - ' + form.cleaned_data['InputFullName']
            email = form.cleaned_data['InputEmail']
            content = 'Hi Startup, \n' + form.cleaned_data['InputQuery'] + '\nRegards\n' + form.cleaned_data['InputFullName'] + '\n' + form.cleaned_data['InputNumber']

            send_mail(
                subject,
                content,
                email,
                ['parfaithrm@gmail.com']
            )

            content = {
                'form': form,
                'title' : 'Services',
                'css' : 'css/services.css',
                'message':'Query sent successfully',
            }

            return render(request, 'portfolio/services.html', content) 
    else:
            form = ContactForm()

    content = {
        'form': form,
        'title' : 'Services',
        'css' : 'css/services.css',
    }

    return render(request, 'portfolio/services.html', content)

def clientele(request):    
    
    files = os.listdir(os.path.join(settings.BASE_DIR, "static/images/clientele/"))
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Query - ' + form.cleaned_data['InputFullName']
            email = form.cleaned_data['InputEmail']
            content = 'Hi Startup, \n' + form.cleaned_data['InputQuery'] + '\nRegards\n' + form.cleaned_data['InputFullName'] + '\n' + form.cleaned_data['InputNumber']

            send_mail(
                subject,
                content,
                email,
                ['parfaithrm@gmail.com']
            )

            content = {
                'form': form,
                'title' : 'Clientele',
                'css' : 'css/clientele.css',
                'message':'Query sent Successfully',
                'files' : files,
                'images' : 0,
            }

            return render(request, 'portfolio/clientele.html', content) 
    else:
            form = ContactForm()
    


    content = {
        'form': form,
        'title' : 'Clientele',
        'css' : 'css/clientele.css',
        'files' : files,
        'images' : 0,
    }

    return render(request, 'portfolio/clientele.html', content)

def opportunities(request):

    jobs = Job.objects.all()

    job_filter = JobFilter(request.GET, queryset=jobs)
    jobs = job_filter.qs

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Query - ' + form.cleaned_data['InputFullName']
            email = form.cleaned_data['InputEmail']
            content = 'Hi Startup, \n' + form.cleaned_data['InputQuery'] + '\nRegards\n' + form.cleaned_data['InputFullName'] + '\n' + form.cleaned_data['InputNumber']

            send_mail(
                subject,
                content,
                email,
                ['parfaithrm@gmail.com']
            )

            return redirect('/opportunities/') 
    else:
            form = ContactForm()

    content = {
        'form': form,
        'jobs' : jobs,
        'filter' : job_filter,
        'title' : 'Opportunities',
        'css' : 'css/opportunities.css',
    }

    return render(request, 'portfolio/opportunities.html', content)

def dropbox(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            subject = 'CV - ' + form.cleaned_data['InputName']
            email = form.cleaned_data['InputEmail']
            content = 'Hi Startup, \n' + '\nRegards\n' + form.cleaned_data['InputName'] + '\n' + form.cleaned_data['InputNumber']
            cv = request.FILES['InputCV']

            msg = EmailMultiAlternatives(
                subject,
                content,
                email, 
                ['parfaithrm@gmail.com']
            )
            msg.attach("curriculum-vitae.pdf",cv.content_type,"application/pdf")
            msg.send()


            content = {
                'form': form,
                'title' : 'Dropbox',
                'css' : 'css/dropbox.css',
                'message':'CV sent Successfully',
            }

            return render(request, 'portfolio/dropbox.html', content) 
    else:
        form = CVForm()

    content = {
        'form': form,
        'title' : 'Dropbox',
        'css' : 'css/dropbox.css',
    }

    return render(request, 'portfolio/dropbox.html', content)

@unauthenticated_user
def managerRegister(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')  

    content = {
        'form':form
    }

    return render(request, 'portfolio/job-register.html', content)

@unauthenticated_user
def managerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('vacancy-dashboard')

        else :
            messages.info(request, 'Username or Password is Incorrect')

    return render(request, 'portfolio/job-login.html')

def managerLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['editors','staff'])
def dashboard(request):
    
    jobs = Job.objects.all()

    job_filter = JobFilter(request.GET, queryset=jobs)
    jobs = job_filter.qs

    content = {
        'jobs' : jobs,
        'filter' : job_filter,
        'title' : 'Job Dashboard',
        'css' : 'css/jobdash.css',
    }

    return render(request, 'portfolio/job-dash.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=['editors','staff'])
def addVacancy(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('vacancy-dashboard') 
    else:
        form = JobForm()

    content = {
        'form': form,
        'title' : 'Add Jobs',
        'css' : 'css/form.css',
    }

    return render(request, 'portfolio/job-add.html', content)

@login_required(login_url='login')
@allowed_users(allowed_roles=['editors','staff'])
def editVacancy(request, pk):
    
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()

            return redirect('vacancy-dashboard') 

    content = {
        'form' : form,
        'title' : 'Edit Jobs',
        'css' : 'css/form.css',
    }

    return render(request, 'portfolio/job-edit.html', content)
    
@login_required(login_url='login')
@allowed_users(allowed_roles=['editors','staff'])
def delVacancy(request, pk):
    job_del = Job.objects.get(id=pk)
    job_del.delete()
    return redirect('vacancy-dashboard') 