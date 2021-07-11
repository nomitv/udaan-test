from django.db import models

# Create your models here.
class AdminUser(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)