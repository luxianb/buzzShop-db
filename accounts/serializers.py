from rest_framework import fields, serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'is_superuser')
        # fields = '__all__'

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)