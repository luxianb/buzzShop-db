# from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.views import View
from .models import Product, Store
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer


# Create your views here.
class StoreView( ):
  def get(self, req):
    return JsonResponse({"hello":"world", "method": req.method})

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.AllowAny]