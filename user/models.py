from distutils.command.upload import upload
from email.mime import image
# from re import T
import django
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True )
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='Profile_Images')

    def __str__(self):
        return f'{self.staff.username}-Profile'


