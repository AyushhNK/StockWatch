from rest_framework import serializers
from django.contrib.auth import authenticate
from apps.accounts.models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "tier", "timezone", "preferred_currency")
