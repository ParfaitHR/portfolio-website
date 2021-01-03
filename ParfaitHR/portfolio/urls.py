from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('services/',views.services, name='services'),
    path('clientele/',views.clientele, name='clientele'),
    path('opportunities/',views.opportunities, name='opportunities'),
    path('dropbox/',views.dropbox, name='dropbox'),

    path('job-vacancy/register/', views.managerRegister, name='register'),
    path('job-vacancy/login/', views.managerLogin, name='login'),
    path('job-vacancy/logout/', views.managerLogout, name='logout'),
    path('job-vacancy/dashboard/',views.dashboard, name='vacancy-dashboard'),
    path('job-vacancy/add/',views.addVacancy, name='add-vacancy'),
    path('job-vacancy/edit/<str:pk>',views.editVacancy, name='edit-vacancy'),
    path('job-vacancy/delete/<str:pk>',views.delVacancy, name='del-vacancy'),
]
