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
from rest_framework.permissions import IsAuthenticated

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
        counts = Account.objects.filter(username=username).count()
        if counts:
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

class AccountDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # print(request.META.get('HTTP_AUTHORIZATION'))
        # print(request.data)
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        print(token)
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        print(type(user_obj))
        serializer = AccountDetailSerializer(instance=user_obj)
        return Response(serializer.data, status=HTTP_200_OK)
        # if(serializer.is_valid()):
        #     return Response(serializer.data, status=HTTP_200_OK)
        # print(serializer.errors)
        # return Response(data={'username':user_obj.username},status=HTTP_400_BAD_REQUEST)

class CreateCollectionAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request, format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        print(user_obj)
        try:
            collects = Collections.objects.filter(user=user_obj.id)
        except:
            return Response(data={"msg":"No Colletions!"},status=HTTP_400_BAD_REQUEST)
        
        serializer = CollectionSerializer(instance=collects, many=True)
        return Response(serializer.data,status=HTTP_200_OK)


    def post(self, request, format=None):
        print(request.data)
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        temp=request.data
        temp['user']=user_obj.id
        collect = CollectionSerializer(data=temp)
        if collect.is_valid():
            collect.save()
            print("i'm in!")
            return Response(data={"msg":'collection create success!'},status=HTTP_200_OK)
        print(collect.errors)
        return Response(status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        print('delete')
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        print(request.data)
        try:
            coll = Collections.objects.get(name=request.data['name'],user=user_obj.id)
        except :
            return Response(data={'msg':"doesn't exist!"},status=HTTP_400_BAD_REQUEST)

        coll.delete()
        return Response(data={'msg':'already delete!'},status=HTTP_200_OK)
        

class AddBookAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        token=request.data['token']
        token_obj=Token.objects.get(key=token)
        user_obj = token_obj.user
        serializer = AccountDetailSerializer(data=user_obj)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request, format=None):
        token=request.data['token']
        token_obj=Token.objects.get(key=token)
        user_obj = token_obj.user
        book_title = request.data['title']
        collection_name = request.data['c_name']









  
        

            


