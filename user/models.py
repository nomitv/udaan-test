from django.db import models
from symptoms.models import Symptoms
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)
    symptoms = models.ManyToManyField(Symptoms, blank=True)
    travel_history = models.BooleanField(default=False, blank=True, null=True)
    contact_with_covid = models.BooleanField(default=False, blank=True, null=True)
    result = models.BooleanField(blank=True, null=True)