from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CartItem)
admin.site.register(models.Store)
admin.site.register(models.Product)
admin.site.register(models.Tags)
admin.site.register(models.StoreBanner)