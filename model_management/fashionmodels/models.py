import uuid
from django.db import models

# Create your models here.

# Inherit from class models.Model. Makes it
# an official Django model

class FashionModel(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  display_image = models.ImageField(upload_to='images', default='./images/placeholder.jpg', height_field=None, width_field=None, max_length=None)
  name = models.CharField(max_length=50)
  height = models.FloatField()
  weight = models.FloatField()
  bust = models.FloatField()
  waist = models.FloatField()
  hip = models.FloatField()
  date_of_birth = models.DateField(auto_now=False, auto_now_add=False)