from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Product
        # the fields that should be included in the serialized output
        fields = ['id', 'store', 'name', 'description', 'price', 'amount']