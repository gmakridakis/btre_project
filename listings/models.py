from django.db import models
from realtors.models import Realtor
from django.utils import timezone

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(max_length=256, blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    area = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to="photos/{%Y/%m/%d/", blank=True)
    photo_two = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_three = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_four = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_five = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_six = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    list_date = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title