from email.mime import application
from multiprocessing.spawn import import_main_path
from unicodedata import name
from django.contrib import admin
from django.urls import path
from MyApp import views


urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("application_form",views.application_form,name='application_form'),
    path("contact",views.contact,name='contact')
]
