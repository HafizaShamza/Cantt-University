
import email
import re
from django.shortcuts import render,HttpResponse
from datetime import datetime
from MyApp.models import Application, Contact
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is a Home page")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is a About page")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is a Services page")
def application_form(request):
    if request.method=="POST":
        name=request.POST.get("name")
        father=request.POST.get("father")
        id_number=request.POST.get("id_number")
        email=request.POST.get("email")
        number=request.POST.get("number")
        application_form=Application(name=name,father=father,id_number=id_number,email=email,number=number,date=datetime.today() )
        application_form.save()
        messages.success(request, "Congratulations! Your Form has been submited. ")

    return render(request,'application_form.html')

    # return HttpResponse("This is a Application Form page")
def contact(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        contact=Contact(email=email,password=password,date=datetime.today())
        contact.save()
        messages.success(request, "Your request has been sent!")
    return render(request,'contact.html')
    # return HttpResponse("This is a Contact Us page")