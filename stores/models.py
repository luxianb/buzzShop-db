from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Store(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name}'

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.FloatField()
  amount = models.IntegerField()
  store = models.ForeignKey(Store, on_delete=models.CASCADE)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  image_url = models.TextField(blank=True)
  cloudinary_id = models.TextField(blank=True)
  tags = models.JSONField(blank=True, default=list)

  def __str__(self):
    return f'{self.name} (prod_id:{self.id}) - ${self.price}'

class CartItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  amount = models.IntegerField(default=1)
  status = models.CharField(max_length=20, default="In cart")

  def __str__(self):
    return f'{self.product} x {self.amount} - {self.user}'

class Review(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
  text = models.TextField(blank=True)

