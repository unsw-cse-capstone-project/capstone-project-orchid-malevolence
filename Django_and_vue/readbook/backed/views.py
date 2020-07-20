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


# 获取token
class CustomAuthToken(ObtainAuthToken):
    # 已测试，无问题
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            ob=serializer.validated_data
            print(ob)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username,'user_id':user.id},status=HTTP_200_OK)
        print(serializer.errors)
        username = request.data['username']
        # 因为名字是唯一的，所以就直接检查名字存不存在就行，存在就说明密码错了，不存在那就不存在。
        counts = Account.objects.filter(username=username).count()
        if counts:
            return Response(data={'msg':"Please Check Your Password!"} ,status=HTTP_400_BAD_REQUEST,content_type='application/json')
        return Response(data={'msg':"User doesn't exist!"} ,status=HTTP_400_BAD_REQUEST,content_type='application/json')

# 注册用户，成功并返回token
class RegisterAPIView(APIView):
    
    # 已经多次测试，无问题
    def post(self, request, format=None):
        print(request.data)
        res = RegSerializer(data = request.data, context={'request': request})
        username = request.data['username']
        if res.is_valid():
            res.save()
            user = Account.objects.get(username=username)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username,'user_id':user.id},status=HTTP_200_OK)
        print(res.errors)
        return Response(data={'msg':"Username is exist!"} ,status=HTTP_400_BAD_REQUEST,content_type='application/json')

# 获取用户信息，包含collection，以及collection里面的books
class AccountDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # 已经无问题
    # 除了包含用户的基本信息之外
    # 还有用户的collection
    # 已经每个collection里面包含的书籍信息
    def get(self, request, format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        print(token)
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        print(type(user_obj))
        serializer = AccountDetailSerializer(instance=user_obj)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self,request,format=None):
        user_id=request.data['id']
        user_obj=Account.objects.get(id=user_id)
        user_obj.date_of_birth=request.data['date_of_birth']
        user_obj.gender = request.data['gender']
        user_obj.save()
        return Response(data={"msg":"edit success!"},status=HTTP_200_OK)

# colloection操作，添加，删除，修改名称
class CreateCollectionAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # 已测试
    def get(self,request, format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        print(user_obj)
        collect_set = Collection.objects.filter(user=user_obj.id)
        if(collect_set.exists()):
            serializer = CollectionSerializer(instance=collect_set, many=True)
            return Response(serializer.data,status=HTTP_200_OK)
        else:
            return Response(data={"msg":"No Colletions!"},status=HTTP_400_BAD_REQUEST)
        

    # 建立新的collection和collection改名，都测试过了
    # 就是跟书籍添加进入collection，会有路由冲突，目前经过调整，阶段性解决。
    def post(self, request, format=None):
        try:
            print(request.data)
            collect_id = request.data['collection_id']
        except:
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
        
        new_name = request.data['name']
        collection_temp = Collection.objects.get(id=collect_id)
        collection_temp.name=new_name
        collection_temp.save()
        return Response(data={"msg":'name change success'},status=HTTP_200_OK)
    
    # 已测试
    def delete(self, request, format=None):
        print('delete')
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        print(request.data)
        collection_id = request.data["collection_id"]
        Collection.objects.filter(id=collection_id,user=user_obj.id).delete()
        return Response(data={'msg':'already delete!'},status=HTTP_200_OK)
        
# 添加书籍进入数据库
class AddBookAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format=None):
        book_info = request.data['book_info']
        book_set=Book.objects.filter(id=book_info["id"])
        if(book_set.exists()):
            return Response(data={"msg":"already in database!"},status=HTTP_200_OK)
        else:
            serializer = BookSerializer(data=book_info)
            if(serializer.is_valid()):
                serializer.save()
                return Response(data={"msg":"add it success"},status=HTTP_200_OK)
            print(serializer.errors)
            return Response(data={"mag":"error"},status=HTTP_400_BAD_REQUEST)

# 搜做书籍
class SearchBookAPIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        search_type = request.data['search_type']
        if search_type.lower() == "title":
            search_key = request.data['key_word']
            search_set = Book.objects.filter(title__contains = search_key)
            if search_set.exists():
                serializer = BookSerializer(instance=search_set,many=True)
                return Response(serializer.data,status=HTTP_200_OK)
            else:
                return Response(data={"msg":"no result!"},status=HTTP_400_BAD_REQUEST)
        elif search_type.lower() == 'authors':
            search_key = request.data['key_word']
            search_set = Book.objects.filter(authors__contains = search_key)
            if search_set.exists():
                serializer = BookSerializer(instance=search_set,many=True)
                return Response(serializer.data,status=HTTP_200_OK)
            else:
                return Response(data={"msg":"no result!"},status=HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"msg":"search type error!"},status=HTTP_400_BAD_REQUEST)
        
    def get(self,request,format=None):
        data=request.query_params
        print(data)
        search_key=data['key_word']
        search_type=data['search_type']
        if search_type.lower() == "title":
            search_set = Book.objects.filter(title__contains = search_key)
            if search_set.exists():
                serializer = BookSerializer(instance=search_set,many=True)
                return Response(serializer.data,status=HTTP_200_OK)
            else:
                return Response(data={"msg":"no result!"},status=HTTP_400_BAD_REQUEST)
        elif search_type.lower() == 'authors':
            search_set = Book.objects.filter(authors__contains = search_key)
            if search_set.exists():
                serializer = BookSerializer(instance=search_set,many=True)
                return Response(serializer.data,status=HTTP_200_OK)
            else:
                return Response(data={"msg":"no result!"},status=HTTP_400_BAD_REQUEST)
        else:
            return Response(data={"msg":"search type error!"},status=HTTP_400_BAD_REQUEST)


# 把书放进collection里面，有待更新
class AddBookToCollectionAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # 基本测试无问题，跟collection建立会有路由冲突，有待解决
    def post(self,request,format=None):
        print(request.data)
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        book_id = request.data["book_id"]
        collection_id = request.data["collection_id"]
        relation_check_set = Collection_Book.objects.filter(collection=collection_id,book=book_id)
        if(relation_check_set.exists()):
            return Response(data={"msg":" this book already in this collection!"},status=HTTP_400_BAD_REQUEST)
        book_obj = Book.objects.get(id=book_id)
        collection_obj = Collection.objects.get(id=collection_id)
        book_collection_relation = Collection_Book(collection=collection_obj,book=book_obj,belongto=user_obj.id)
        book_collection_relation.save()
        return Response(data={"msg":"add it success!"},status=HTTP_200_OK)
    
    # 初步测试无问题，找不到也会成功返回。 
    def delete(self,request,format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        book_id = request.data["book_id"]
        collection_id = request.data["collection_id"]
        Collection_Book.objects.filter(collection=collection_id,book=book_id,belongto=user_obj.id).delete()
        return Response(data={"msg":"delete it success"},status=HTTP_200_OK)


# 添加评论，目前不支持修改和删除
class ReviewAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # 初步测试无问题
    def post(self,request,format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        book_id = request.data['book_id']
        review_info = request.data['review']
        review_info['user']=user_obj.id
        review_info['book']=book_id
        serializer = ReviewSerializer(data=review_info)
        if serializer.is_valid():
            serializer.save()
            print('ready to save')
            return Response(data={'msg':'add review success'},status=HTTP_200_OK)
        print(serializer.errors)
        return Response(data={'msg':'error'},status=HTTP_400_BAD_REQUEST)

# 给书打分,支持修改分数
class RatingAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # decimal小数位有点不对，后面记得改！！！
    def post(self,request,format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        rating_info = request.data['rating_info']
        rating_set=Rating.objects.filter(user=user_obj.id,book=rating_info['book'])
        if(rating_set.exists()):
            # 如果存在，说明之前打过分数，修改就行了
            rating_temp=rating_set[0]
            rating_temp.rating = rating_info['rating']
            rating_temp.save()
            return Response(data={"msg":'update success!'},status=HTTP_200_OK)

        else:
            # 不存在就说明没打过分数，插入数据
            rating_info['user']=user_obj.id
            serializer = RatingSerializer(data=rating_info)
            if serializer.is_valid():
                serializer.save()
                return Response(data={'msg':'add rating success'},status=HTTP_200_OK)
            print(serializer.errors)
            return Response(data={'msg':'error'},status=HTTP_400_BAD_REQUEST)

# 点赞：包括第一次点赞和取消赞
class LikeItAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # 初步检测，应该没问题了
    def post(self,request,format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        review_id = request.data['review_id']
        like_info = request.data['likeit']

        like_set=LikeIt.objects.filter(review=review_id,user=user_obj.id)
        print("i's here")
        if(like_set.exists()):
            if(like_info["status"]==-1):
                # 取消点赞，如果已经被取消，则直接返回
                like_new_info = like_set[0]
                if(like_new_info.status==0):
                    return Response(data={"msg":"别折腾了"},status=HTTP_400_BAD_REQUEST)
                like_new_info.status=0
                like_new_info.save()
                review_new_temp=Review.objects.get(id = review_id)
                review_new_temp.like_count_num-=1
                review_new_temp.save()
                return Response(data={'msg':'点赞取消'},status=HTTP_200_OK)
            else:
                # 回复点赞，之前点过，后来取消了，然后又点赞了
                like_new_info = like_set[0]
                if(like_new_info.status==1):
                    return Response(data={"msg":"别折腾了"},status=HTTP_400_BAD_REQUEST)
                like_new_info.status=1
                like_new_info.save()
                review_new_temp=Review.objects.get(id = review_id)
                review_new_temp.like_count_num+=1
                review_new_temp.save()
                return Response(data={"msg":"我又点赞了！"},status=HTTP_200_OK)
            return Response(data={"msg":"already like it!"},status=HTTP_200_OK)
        else:
            print("i'm in!")
            likeit_info = request.data['likeit']
            likeit_info['user']=user_obj.id
            likeit_info['review']=review_id
            likeit_info['belongto_book']=request.data['book_id']
            print("284 284 284")
            serializer = LikeItSerializer(data=likeit_info)
            if serializer.is_valid():
                serializer.save()
                if serializer.data['status']==1:
                    review_temp=Review.objects.get(id=review_id)
                    review_temp.like_count_num+=1
                    review_temp.save()
                return Response(data={'msg':'like it!'},status=HTTP_200_OK)
            print(serializer.errors)
            return Response(data={'msg':'error'},status=HTTP_400_BAD_REQUEST)
    
# 点击某一本书之后，显示的具体信息
# 和userid还有具体的bookid挂钩
# 返回的数据包括：
# 1.user对book的评分
# 2.book的所有评论，以时间为返回顺序
# 3.针对每一条评论，赞的数量
# 4.用户是否对某一条或者多条评论点过赞
class BookDetailPageAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    def get(self,request,format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        data=request.query_params
        book_id = data['book_id']
        book_set = Book.objects.filter(id=book_id)
        if(book_set.exists()):
            book_obj = book_set[0]
            serializer = BookDetailPageSerializer(instance=book_obj,context={'user_id': user_obj.id})
            return Response(serializer.data,status=HTTP_200_OK)
        else:
            return Response(data={"msg":"No Book!"},status=HTTP_400_BAD_REQUEST)


#  
class MonthlyGoalAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    # 简单测试无问题
    # 检查是否已经设定月度目标，没有的话会返回404
    def get(self,request,format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        goal_info= request.data['month']
        print(request.data)
        goal_set = Goal.objects.filter(user=user_obj.id,month=goal_info)
        if(goal_set.exists()):
            goal_data=goal_set[0]
            ans = Collection_Book.objects.filter(belongto=user_obj.id,create_time__month=goal_info)
            num=0
            if(ans.exists()):
                num=ans.count()
            return Response(data={"target":goal_data.target,"already_done":num},status=HTTP_200_OK)
        else:
            return Response(data={"msg":"goal have not set yet!"},status=HTTP_400_BAD_REQUEST)   

    # 设定每月目标，在第一次设定时会检查并返回当月已经添加的书籍
    # 修改目标，每次也会重新检查并返回数据
    def post(self,request,format=None):
        token=request.META.get('HTTP_AUTHORIZATION')
        token=token.split()
        token_obj=Token.objects.get(key=token[1])
        user_obj = token_obj.user
        goal_info = request.data['month_goal']
        goal_info['user']=user_obj.id
        goal_set = Goal.objects.filter(user=user_obj.id,month=goal_info['month'])
        if(goal_set.exists()):
            goal_temp = goal_set[0]
            goal_temp.target = goal_info['target']
            goal_temp.save()
            ans = Collection_Book.objects.filter(belongto=user_obj.id,create_time__month=goal_info['month'])
            num=0
            if(ans.exists()):
                num=ans.count()
            return Response(data={"msg":"edit set success","already_done":num},status=HTTP_200_OK)
        else:
            serializer = MonthlyGoalBaseSerializer(data=goal_info)
            if(serializer.is_valid()):
                serializer.save()
                # res = MonthlyGoalAPIView(isinstance=goal_info)
                ans = Collection_Book.objects.filter(belongto=user_obj.id,create_time__month=goal_info['month'])
                num=0
                if(ans.exists()):
                    num=ans.count()
                return Response(data={"msg":"set success","already_done":num},status=HTTP_200_OK)
            print(serializer.errors)
            return Response(data={"msg":"errors"},status=HTTP_400_BAD_REQUEST)




        
















  
        

            


