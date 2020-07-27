from account.models import *
from backed.models import *
from .serializers import *
import json
from django_redis import get_redis_connection
con=get_redis_connection("default")

# 简单推荐评分最高的五本书以及被添加数最多的五本书

def mainpagerec():
    main_page_rec_set = Book.objects.all().order_by('-avg_rating','-added_times')[:5]
    serializer = BookSerializer(instance=main_page_rec_set,many=True)
    for i in serializer.data:
        con.rpush('mainpagelist',json.dumps(i))

def getHighRatingBooks():
    book_set=Book.objects.all().order_by('-avg_rating')[:5]
    serializer = BookSerializer(instance=book_set,many=True)
    for i in serializer.data:
        con.rpush('highrating',json.dumps(i))

def getHighAddedBooks():
    book_set=Book.objects.all().order_by('-added_times')[:5]
    serializer = BookSerializer(instance=book_set,many=True)
    for i in serializer.data:
        con.rpush('highadded',json.dumps(i))

def operation():
    mainpagerec()
    getHighAddedBooks()
    getHighRatingBooks()