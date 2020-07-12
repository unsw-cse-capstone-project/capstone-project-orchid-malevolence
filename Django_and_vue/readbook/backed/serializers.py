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
    class Meta:
        model = Book
        fields = ('__all__')
        extra_kwargs = {'collection':{'required':False}}

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
        fields = ['username','email','gender','uimg','date_of_birth','join_date','collections']
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
        if(rating_set.exists()):
            rating_temp=rating_set[0]
            return rating_temp.rating
        else:
            return 0


    def review_edit(self,obj):
        book_id = obj.id
        review_set = Review.objects.filter(book=book_id)
        if(review_set.exists()):
            rev_ser = ReviewSerializer(instance=review_set,many=True)
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



# class ReviewEditSerializer(serializers.Serializer):
#     content = models.TextField(null=True)
#     create_time = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(Account,related_name='review_user',on_delete=models.CASCADE)
#     book = models.ForeignKey(Book,related_name='review_book',on_delete=models.CASCADE)
#     like_count_num = models.PositiveIntegerField(default=0)
#     user_liked_or_not = models.BooleanField(default=False)

# class BookDetailSerializer(serializers.Serializer):
#     book_id = models.CharField()
#     rating = models.DecimalField(max_digits = 5,decimal_places=2,null=True)
#     reviews = ReviewEditSerializer(many=True,required=False)








