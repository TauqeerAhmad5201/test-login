from django.db import models

# Create your models here.
class Signupdata(models.Model):
    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    password2 = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)