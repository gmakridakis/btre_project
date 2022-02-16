from django.db import models
from django.utils.timezone import now

# Create your models here.

class Contact(models.Model):
     listing = models.CharField(max_length=200)
     listing_id = models.IntegerField()
     name = models.CharField(max_length=200)
     email = models.CharField(max_length=100)
     phone = models.CharField(max_length=30)
     message = models.CharField(max_length=400, blank=True)
     contact_date = models.DateField(default=now, blank=True)
     user_id = models.IntegerField(blank=True)


     def __str__(self) -> str:
         return self.name