from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PoliceStationProfile(models.Model):
    profile = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    # name = models.CharField(max_length=255)
    address = models.TextField()
    incharge_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.profile.first_name+self.profile.last_name
    