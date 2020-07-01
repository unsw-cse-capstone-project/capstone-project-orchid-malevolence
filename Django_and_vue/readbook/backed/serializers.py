from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from account.models import *
from .models import *

class RegSerializer(serializers.ModelSerializer):
    checkpass = serializers.CharField(max_length=256, write_only=True)
    # gender = serializers.CharField(max_length=256)

    class Meta:
        model = Account
        fields = ('username', 'password', 'checkpass', 'email')
        extra_kwargs = {'checkpass': {'required': False}}
    
    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        del attrs['checkpass']
        return attrs

# 这个用于login验证
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'password')

# book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title','authors','publisher')

#collection

class CollectionSerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True)
    class Meta:
        model = Collections
        fields = ('name','user')

# 这个用于访问用户账户页面以及添加图书等
class AccountDetailSerializer(serializers.ModelSerializer):
    collections = CollectionSerializer(many=True)
    class Meta:
        model = Account
        fields = ['username','email','gender','collections']
        # fields = "__all__"
        # exclude = ('password',)


