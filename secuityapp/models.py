from django.db import models

class UserReg(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    fullname=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=12)
    address=models.CharField(max_length=500)
    
