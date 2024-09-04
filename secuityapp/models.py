from django.db import models
from datetime import date
class UserReg(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    fullname=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=12)
    address=models.CharField(max_length=500)
class Profile(models.Model):
    aboutme=models.CharField(max_length=500)
    hobby=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    createdate=models.DateField(null=True, blank=True, default=date.today())
    
class Job(models.Model):

    jobtitle = models.CharField(max_length=100)

    jobdescription = models.CharField(max_length=500)
