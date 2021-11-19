from django.db import models
from django.utils import timezone

class Realtor(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="photos/realtors/%Y%m%d/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name