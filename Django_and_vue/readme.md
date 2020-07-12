
# Require
1.install virtual env
```
sudo pip3 install virtualenv
```
High recommand for python3(pip3), some packet cannot run on python2(pip)! 

2.create a virtual envirment for your project
```
cd your_project_bame
virtualenv venv
```
3. and you can find a dic named venv 
4, start virtualenv
```
source venv/bin/activate
```
5.install all requirments
```
pip install -r requirements.txt
```

# how to run it
cd to the root dir which contains manage.py file.<br>
```
python manage.py runserver
```
if your default python command is python2, you need use python3 to replace python!<br>
you can use this to know python version:
```
python --version
```
if your terminal show this: Congratulations！your server is running!
![image](https://github.com/unsw-cse-capstone-project/capstone-project-orchid-malevolence/blob/master/Django_and_vue/img.png)

And now, you can check all data with admin account, or get data with your vue with api.

# account(username and password)
please use normal account priority:
Black,123456<br>
Pink,123456<br>

Superuser account: username: admin, password: 123456<br>
localhost:8000/admin<br>
you can create an new account, do not use complex password, if account be created, password will be Encrypted! you can not check it by /admin!

# api-guidelines
```
base-url: http://127.0.0.1:8000/
```
## login
```
url: /api/login/
```
1. username and password are correct, data will contain token.
2. password is incorrect, data will contain error message, named "msg".
3. user doesn't exist, data will contain error message, named "msg".

your data should look like this:
```
{
    "username": "Pink",
    "password": ######
}
```

## register
```
url: /api/register/
```

1. success, return token
2. error, will return error msg!

your data is a form, it should like this
```
{
    "username": "Pink",
    "password": ######,
    "checkpass": ######(same as password),
    "email": "poink@163.com"
}
```

## account detail
```
url: /api/account/
```
this request does not need any extra info, i can get account token by header. Or you can sens ti with json data.

it will return a json data, which contain the whole info of user except password.

## collection operations
```
url: /api/collection/
```
1.get:
you can acquire the collection set of user
this operation does not need any extra info

the response data contain all collections and books be stored in collections.

the data like this:
```
[
    {
        "id": 2,
        "name": "pink's collection",
        "user": 3,
        "books": [
            {
                "id": "h56ansk4Sabc",
                "title": "java: Web develop",
                "authors": "liuminghao",
                "publisher": "unsw",
                "publish_date": "2015-08-09",
                "page_count": 120,
                "categories": "science",
                "ISBN": 9780819602899,
                "averageRating": "4.40",
                "description": "it is a interesting book, whcih can tecah you how to desgin a java program!",
                "imageLink": "http://books.google.com/books/content?id=h56ansk4SyQC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                "collection": [
                    2
                ]
            },
            {
                "id": "h56ansk4Syzk",
                "title": "python: mechine learing",
                "authors": "liuminghao",
                "publisher": "unsw",
                "publish_date": "2017-03-09",
                "page_count": 120,
                "categories": "science",
                "ISBN": 9780819602867,
                "averageRating": "4.40",
                "description": "it is a interesting book, whcih can tecah you how to desgin a java program!",
                "imageLink": "http://books.google.com/books/content?id=h56ansk4SyQC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
                "collection": [
                    2
                ]
            }
        ]
    },
    {
        "id": 3,
        "name": "collection_2",
        "user": 3,
        "books": []
    }
]
```

2.post:
you can add a collection with name to user

your data shoud be:
```
create new :
{
    "name":"collection_1"
}

if re-name:
{
    "collection_id":1,
    "name":"Pink's collection"
}
```

3.delete:
you can delete a collection with name

```
{
    "collection_id":1
}
```

4

# book operations

this part have two main functions:
1.add book to db
2.add book which is already in db to collection


## add book to db
```
url: /api/add_book_to_db/
```

only one opeartion post
your data structure should like this:
```
    "book_info": {
        "id":"h56ansk4Sqpk",
        "title": "php: God language",
        "authors": "liuminghao",
        "publisher":  "unsw",
        "publish_date":"2011-08-09",
        "page_count": 120,
        "categories": "science",
        "ISBN":"9780819659867",
        "averageRating":4.4,
        "description":"it is a interesting book, whcih can tecah you how to desgin a java program!",
        "imageLink":"http://books.google.com/books/content?id=h56ansk4SyQC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api"
    }
```

!!!!! id is unique and ISBN is unique !!!!!!!!

## add book to collection
```
url: /api/add_to_collection
```

1.post:

```
{
    "collection_id":2,
    "book_id":"h56ansk4Sabc"
}
```
hits:
if you can do this, you have already acquire collection_id and book infomation which contain book id.!!!

3.delete:
this operation base on this situation: the book already in db and be added in one collection or some collections.

```
{
    "collection_id":2,
    "book_id":"h56ansk4Sabc"
}
```
you want to add this book to this collection or remove this book from this collection.

# set monthly goal
```
url: /api/set_goal/
```
1.get:
you can acquire goal data, which contain target and already done count num
you can send data:
```
{
    "month":7
}
```
the response:
```
{
    "target": 0,
    "already_done": 2
}
```
2.post:
create new goal or edit goal.
request data:
```
{
    "month_goal":
    {
        "month":7,
        "target"2
    }
}
```
response:
```
{   "msg":set success!
    "already_done": 2
}
```

# rating
```
url: /api/rating/
```
post:
request data:
```
{
    "rating_info":{
        "book":"h56ansk4Sabc",
        "rating":3.5
    }
}
```

you can check the respnse status.

# review
```
url: /api/review/
```

can not support edit and delet!

post:
request data:
```
{
    "book_id":"h56ansk4Sabc",
    "review":{
        "content":"2 years later, this still tech me so much! I recommand this book significantly!"
    }
}
```

no key data in response, check the status.

# like it
```
url: /api/likeit/
```
post:

request data:
```
{
    "review_id":1,
    "book_id":"h56ansk4Sabc",
    "likeit":{
        "status":1        
    }
}
```

status: 
1 == like
-1 == un like

# book detail page
```
url: /api/bookdetail/
```
get:

your request data:
```
{
    "book_id":"h56ansk4Sabc"
}
```

response:
```
{
    "id": "h56ansk4Sabc",
    "title": "java: Web develop",
    "rating": 3.5,
    "user_like_which": [
        {
            "id": 1,
            "status": true,
            "belongto_book": "h56ansk4Sabc",
            "review": 1,
            "user": 3
        }
    ],
    "review_book": [
        {
            "id": 1,
            "content": "This book is very userful, and the author is a good coder!",
            "user": 3,
            "book": "h56ansk4Sabc",
            "like_count_num": 1
        },
        {
            "id": 2,
            "content": "2 years later, this still tech me so much! I recommand this book significantly!",
            "user": 3,
            "book": "h56ansk4Sabc",
            "like_count_num": 0
        }
    ]
}
```

response data contain these:
1.book id : "id"
2.book titel: "title
3.rating by user: "rating" (this is not the avg rating)
4.user like which review, you can check the "user_like_which"-> "review", this is the review id
5. all review relate to this book:
    for each review, contain:
        review centene:"content"
        who write this review:  "review_book" -> "user"
        how many peoplw like this review: "review_book" -> "like_count_num"
                                    



# to be continue

## recommand system
## rating optimiza
## more data


# file structure
```
.
├── account
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── backed
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── readbook
    ├── __init__.py
    ├── __pycache__
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```
