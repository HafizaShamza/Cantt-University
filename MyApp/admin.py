import imp
from django.contrib import admin
from MyApp.models import Application
from MyApp.models import Contact
# Register your models here.
admin.site.register(Application)
admin.site.register(Contact)
