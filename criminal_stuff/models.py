from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField,JSONField
import os

# Create your models here.

# class CrimeCommitted(models.Model):
#     crime = models.CharField(max_length=255)
#     booked_on = models.DateTimeField(auto_now_add=True)
#     booked_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     crime_description = models.TextField()

#     def __str__(self):
#         return self.crime_description

class Criminal(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    # crimes = models.ForeignKey(CrimeCommitted,on_delete=models.CASCADE)
    crime_category = models.CharField(max_length=255, blank=True, null=True)
    booked_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    booked_at_police_station = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    crime_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/criminal_images',blank=True, null=True)
    image_data = ArrayField(models.FloatField(), blank=True, null=True)

    def __str__(self):
        return self.name
    

    

