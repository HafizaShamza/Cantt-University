
from django.db import models


# Create your models here.
## Admission Class
class Application(models.Model):
    name=models.CharField(max_length=100)
    father=models.CharField(max_length=100)
    id_number=models.CharField(max_length=13)
    email=models.CharField(max_length=30)
    number=models.CharField(max_length=12)
    date=models.DateField()

    def __str__(self):
        return self.name

## Contact class
class Contact(models.Model):
   
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    date=models.DateField()
    
    def __str__(self):
        return self.email
    
