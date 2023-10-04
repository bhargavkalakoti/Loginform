from django.db import models

class Login(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    Phone=models.CharField(max_length=10)
    email=models.EmailField()
    