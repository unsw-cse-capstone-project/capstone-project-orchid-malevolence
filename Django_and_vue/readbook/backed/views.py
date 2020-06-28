from django.shortcuts import render
from account.models import *
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import *

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            ob=serializer.validated_data
            print(ob)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username})
        print(serializer.errors)
        username = request.data['username']
        # 因为名字是唯一的，所以就直接检查名字存不存在就行，存在就说明密码错了，不存在那就不存在。
        countn = Account.objects.filter(username=username).count()
        if countn:
            return Response(data={'msg':"Please Check Your Password!"} ,status=HTTP_400_BAD_REQUEST,content_type='application/json')
        return Response(data={'msg':"User doesn't exist!"} ,status=HTTP_400_BAD_REQUEST,content_type='application/json')

class RegisterAPIView(APIView):

    def post(self, request, format=None):
        print(request.data)
        res = RegSerializer(data = request.data, context={'request': request})
        username = request.data['username']
        if res.is_valid():
            res.save()
            user = Account.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username})
        print(res.errors)
        return Response(data={'msg':"Username is exist!"} ,status=HTTP_400_BAD_REQUEST,content_type='application/json')

  
        

            


