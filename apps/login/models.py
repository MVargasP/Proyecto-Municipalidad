from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager



class User(AbstractUser):
    dni	= models.CharField('DNI/ PTP/ Cedula',null=True,max_length=10)
    username = models.CharField('Usuario', max_length=150,primary_key=True)

    def __str__(self):
       return str(self.username)
