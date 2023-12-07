from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
            model = User
            fields = ('username', 'password')

