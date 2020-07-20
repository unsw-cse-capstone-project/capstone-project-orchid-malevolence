
# Require
1.install virtual env.
```bash
sudo pip3 install virtualenv
```
High recommand for python3(pip3), some packet cannot run on python2(pip)! 

2.create a virtual envirment for your project.
```bash
cd your_project_bame
virtualenv venv
```
3. and you can find a dic named venv.
4. start virtualenv.
```
source venv/bin/activate
```
5.install all requirments.
```
pip install -r requirements.txt
```

# How to run it
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

# Account(username and password)
please use normal account priority:
Black,123456<br>
Pink,123456<br>

Superuser account: username: admin, password: 123456<br>
localhost:8000/admin<br>
you can create an new account, do not use complex password, if account be created, password will be Encrypted! you can not check it by /admin!

# Book Datbase
database have 300 books information.

these book related to
```python
['python','java','linux','harryporter','Holmes','Django','Twilight','cook',
    # 'Shakespeare','hugo','Algorithm','Vampire','Verne','Ocean','Food','Fruit','Maya','Egypt','Roma',
    # 'Carthage','United Kingdom','Blues','Rock','sex','education','love','friend','countryside','airplane','magic','speaking']
```

# Api-guidelines
```
base-url: http://127.0.0.1:8000/
```
## Login
```
url: /api/login/
```
>POST

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

## Register
```
url: /api/register/
```

>POST

1. success, return token
2. error, will return error msg!
3. it will create a default collection named  "username's collection"

your data is a form, it should like this
```
{
    "username": "Pink",
    "password": ######,
    "checkpass": ######(same as password),
    "email": "poink@163.com"
}
```

## Account detail
```
url: /api/account/
```

>GET

获取当前用户的基本信息，包括collections，以及colelction下面的book

this request does not need any extra info, i can get account token by header. Or you can sens ti with json data.

it will return a json data, which contain the whole info of user except password.

>POST

目前支持修改用户的性别和生日，都以“字符串”类型发送过来！！
发送的json中必须都要包含性别和生日，不修改也要放进去：
```json
{
    "id":3,
    "gender":"male"/"female",
    "date_of_birth":"2020-06-06"
}
```

性别这里我后端没有做任何的字符串筛选！
生日日期最好为字符串！

## Collection operations
```
url: /api/collection/
```

>GET

返回数据如下

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

you can acquire the collection set of user
this operation does not need any extra info

the response data contain all collections and books be stored in collections.


>POST

就是建立新的collection，包含colelction的名字，原则上最好别重复，但是也可以，最好前端判断一下，如果有重名就需要修改。

you can add a collection with name to user

your data shoud be:
```
create new :
{
    "name":"collection_1"
}

```


>DELETE

删除colleciton，发送colelction的id就行了

你的axios数据参数：
```js
axios.delete(url, {data:{collection_id:1}})
```

you can delete a collection with name

```
{
    "collection_id":1
}
```

>PUT 

修改collection名字

```js
axios.put(url, {collection_id:1, new_name: #####})
```



# Book operations

1.add book to db
2.add book which is already in db to collection
3.search book with title or authors


## Add book to db
```
url: /api/add_book_to_db/
```

>POST

这个是单独开放的接口，往数据库里面插入书籍。
插入要求如下：
其中id和isbn都是唯一的

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

## Add book to collection
```
url: /api/add_to_collection
```

>POST add the book to the collection

把书加入colleciton中，需要发送collection id和书的id

```
{
    "collection_id":2,
    "book_id":"h56ansk4Sabc"
}
```
hits:
if you can do this, you have already acquire collection_id and book infomation which contain book id.!!!

>DELETE

把某本书从collection中删掉。
目前不支持批量删除。

你的axios数据参数应当如下：
```js
axios.delete(url, {data: {collection_id:1, book_id:h56ansk4Sabc}})
```

this operation base on this situation: the book already in db and be added in one collection or some collections.

```
{
    "collection_id":2,
    "book_id":"h56ansk4Sabc"
}
```
you want to add this book to this collection or remove this book from this collection.

## Search book

```
url: /api/searchbook/
```

！！！！！ 我get和post都做了接口，爱用哪个用哪个，get用params参数，post用body参数 ！！！！！

>POST search some book with title or authors.

搜索书籍，通过post方法。
请求数据包含搜索类型和搜索关键词
有结果会返回书籍的object的list。
如果没有就返回400.（有待商榷）

```
{
    "search_type": "Title"/"Authors",
    "key_word": "python"
}
```

return all book objects related to "key_word"
if no result, it will return error msg and status 400.

# Set monthly goal
```
url: /api/set_goal/
```


>GET params参数传递
这个就是简单的获取目标的值。

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
>POST set the goal value and edit goal value

使用post方法
进行设置目标，或者修改目标。
发送规定格式的数据：
    month是当前月份，最好通过vue函数获取。
    target就是目标数字。
    不能为负数！
    
返回数据包括返回信息，是否成功，
还有多少已经完成的数量。
（就是当前月份被加入user任意的collection的书的数量。）

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

# Rating
```
url: /api/rating/
```

>POST user give book a rating

使用post方法

用户对当前书进行打分
发送规定样式的请求数据，request数据包含：
    书籍id，以及分数，最多小数点后一位！！

返回数据为返回状态。

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

# Review
```
url: /api/review/
```

>POST user post a review to one book

使用post，用户对当前图书进行评论。

request需要包含：书的id以及规定格式的评论内容。

返回数据无所谓，判断status就行。

目前不支持评论的修改和删除。

can not support edit and delet!
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

# Like it
```
url: /api/likeit/
```

>POST user like one review

使用post 记录用户对哪个评论点赞。
request数据需要包含评论的id，书的id，以及以及规定格式的是否点赞状态。

用户取消点赞，也是一样，只不过status=-1就行。

返回数据不重要，判断返回数据的status就行。

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
-1 == un-like

# Book detail page
```
url: /api/bookdetail/
```
>GET params参数传递

用get，向地址发送
request信息需要有book_id
返回数据为这个书的基本信息：
包括书的id，书名，评分（包括分数和评分人数）

user_like_which:
    是指当前用户给哪些评论点过赞，这里面的id不是需要的数据。
    这里面每一条数据的review是对应的评论的id

review_book：
    这本书有的所有评论，这下面的每条数据中的id是就是评论自己的id
    content是评论内容
    like_count_num是多少人点过赞。

如果想知道当前用户对哪些评论点过赞，就通过user_like_which中的每一条数据的 "review"来对应查找评论，
如果user_like_which为空，则用户目前未对当前图书下面的评论点过赞。

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


# File structure
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
