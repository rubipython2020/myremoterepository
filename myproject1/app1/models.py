from django.db import models

class Employee_details(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=200)
    dept=models.CharField(max_length=100)
    address=models.CharField(max_length=500)

