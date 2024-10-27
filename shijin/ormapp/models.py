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



# Create your models here.
