from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from account.models import *

class RegSerializer(serializers.ModelSerializer):
    checkpass = serializers.CharField(max_length=256, write_only=True)
    gender = serializers.CharField(max_length=256)

    class Meta:
        model = Account
        fields = ('username', 'password', 'checkpass', 'email', 'gender')
        extra_kwargs = {'checkpass': {'required': False}}
    
    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        del attrs['checkpass']
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        field = ('username', 'password')