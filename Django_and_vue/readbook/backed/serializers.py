from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from account.models import *
from .models import *

# 注册的序列化
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

# book全部信息
class BookSerializer(serializers.ModelSerializer):
    # collections = CollectionSerializer(many=True,require = False)
    avg_rating = serializers.SerializerMethodField('avg_rating_edit',required=False)
    class Meta:
        model = Book
        fields = ('__all__')
        extra_kwargs = {'collection':{'required':False}}
    
    def avg_rating_edit(self,obj):
        book_id=obj.id
        rating_count_set = Rating.objects.filter(book=book_id)
        avg_rating=0
        count_num = rating_count_set.count()
        if(rating_count_set.exists()):
            for i in rating_count_set:
                avg_rating+=i.rating
            avg_rating=avg_rating/count_num
            return avg_rating
        return avg_rating


# collection全部信息，包括有哪些书
class CollectionSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, required = False, read_only=True)
    class Meta:
        model = Collection
        fields = ('id','name','user','books')
    
    # def get_books(self,obj):
    #     relation_set = Collection_Book.objects.filter(collection=obj.id)
    #     book_id_list = []
    #     if(relation_set.exists()):
    #         for i in relation_set:
    #             book_id_list.append(i.book)
            
    #     else:
    #         return book_id_list


# 这个用于访问用户账户页面以及添加图书等
class AccountDetailSerializer(serializers.ModelSerializer):
    collections = CollectionSerializer(many=True, required = False)
    class Meta:
        model = Account
        fields = ['id','username','email','gender','uimg','date_of_birth','join_date','collections']
        # fields = "__all__"
        # exclude = ('password',)

# 评论的信息，
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id','content','user','book','like_count_num']

# 点赞信息，
class LikeItSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikeIt
        fields = ('__all__')

# 打分信息
class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('__all__')

# 每月目标

class MonthlyGoalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('__all__')


# 用户对哪些评论点赞了


# serializer = DeviceByTypeSerializer(device_type, many=True, context={'request': request})
# 书籍详细信息（包含打分，评论，点赞，赞数，评论排序按时间来）
class BookDetailPageSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField('rating_edit',required=False)
    # review_book =ReviewSerializer(many=True,required=False)
    review_book =serializers.SerializerMethodField('review_edit',required=False)
    user_like_which = serializers.SerializerMethodField('like_edit',required=False)
    class Meta:
        model = Book
        fields = ['id','title','rating','user_like_which','review_book']
    
    def rating_edit(self,obj):
        user_id = self.context['user_id']
        book_id = obj.id
        rating_set = Rating.objects.filter(user=user_id,book=book_id)
        rating_count_set = Rating.objects.filter(book=book_id)
        avg_rating=0
        count_num = rating_count_set.count()
        if(rating_count_set.exists()):
            for i in rating_count_set:
                avg_rating+=i.rating
            avg_rating=avg_rating/count_num

        if(rating_set.exists()):
            rating_temp=rating_set[0]
            return {"rating":rating_temp.rating,"how_many_user_scored":count_num,'average_rating':avg_rating}
        else:
            return {"rating":0,"how_many_user_scored":count_num,'average_rating':avg_rating}


    def review_edit(self,obj):
        book_id = obj.id
        review_set = Review.objects.filter(book=book_id)
        if(review_set.exists()):
            rev_ser = ReviewSerializer(instance=review_set,many=True)
            res=[]
            for i in rev_ser.data:
                rating_temp_set=Rating.objects.filter(user=i['user'],book=i['book'])
                if(rating_temp_set.exists()):
                    rating_temp=rating_temp_set[0]
                    i['rating']=rating_temp.rating
                    res.append(i)
                else:
                    i['rating']=0
                    res.append(i)
            return rev_ser.data
        else:
            return [] 
    
    def like_edit(self,obj):
        user_id = self.context['user_id']
        book_id = obj.id
        liked_set = LikeIt.objects.filter(user=user_id,belongto_book=book_id,status=True)
        if(liked_set.exists()):
            like_ser = LikeItSerializer(instance=liked_set,many=True)
            return like_ser.data
        else:
            return []








