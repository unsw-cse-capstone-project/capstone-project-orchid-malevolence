from account.models import *
from backed.models import *
from .serializers import *
import json
from django_redis import get_redis_connection
con=get_redis_connection("default")

# those are simple recommend

# main page recommend books
def mainpagerec():
    main_page_rec_set = Book.objects.all().order_by('-avg_rating','-added_times')[:5]
    serializer = BookSerializer(instance=main_page_rec_set,many=True)
    for i in serializer.data:
        con.rpush('mainpagelist',json.dumps(i))

# recommend five high rating books
def getHighRatingBooks():
    book_set=Book.objects.all().order_by('-avg_rating')[:5]
    serializer = BookSerializer(instance=book_set,many=True)
    for i in serializer.data:
        con.rpush('highrating',json.dumps(i))

# recommend five collection nums books
def getHighAddedBooks():
    book_set=Book.objects.all().order_by('-added_times')[:5]
    serializer = BookSerializer(instance=book_set,many=True)
    for i in serializer.data:
        con.rpush('highadded',json.dumps(i))

# run these function
def operation():
    mainpagerec()
    getHighAddedBooks()
    getHighRatingBooks()