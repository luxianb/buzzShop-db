from django.db import models
from django.conf import settings

# Create your models here.
class Store (models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Product (models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.IntegerField()
  amount = models.IntegerField()
  store = models.ForeignKey(Store, on_delete=models.CASCADE)