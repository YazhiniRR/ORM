# Ex02 Django ORM Web Application
## Date: 26.10.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-10-26 155843.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
from django.db import models
from django.contrib import admin
class Borrower(models.Model):
	Name=models.CharField(max_length=10)
	Accountno=models.IntegerField(primary_key="accountno")
	DoB=models.DateField()	
	Annualincome=models.IntegerField()
	Address=models.CharField(max_length=10)
	Aadharno=models.IntegerField()
class BorrowerAdmin(admin.ModelAdmin):
        list_display=('Name','Accountno','DoB','Annualincome','Address','Aadharno')

from django.contrib import admin
from django.contrib import admin
from.models import Borrower,BorrowerAdmin
admin.site.register(Borrower,BorrowerAdmin)
        



## OUTPUT


Include the screenshot of your admin page.
![alt text](<Screenshot (31).png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
