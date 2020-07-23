
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

# Book Database
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

这个接口没有任何验证要求！！

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

## search filter
```
url: /api/filtersearchbook/
```

>GET

同上没有任何验证要求！！

get请求，参数在params里面
{
    "search_type": "Title"/"Authors",
    "key_word": "python"，
    "filter_rating": 3
}

前面两个跟搜索一样，再额外添加一个筛选分数条件。
最好是整数！！！
会返回大于等于当前筛选分数的结果！！



# Set monthly goal
```
url: /api/set_goal/
```
!!!!!做了修改了！！！！！！

！！！！！post和get都改了 ！！！！！！！！
!!!!添加年份限定！！！
！！！！ 如果之前没设定过目标，除了返回400.也会返回 0，0！！！！！！

>GET params参数传递
这个就是简单的获取目标的值。

you can acquire goal data, which contain target and already done count num
you can send data:

```
{   
    "year":2020,
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
    year,当前年份
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
        "year":2020,
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
    书籍id，以及分数，分数为【1，5】的整数，两边闭包！

返回数据为返回状态。

request data:
```
{
    "rating_info":{
        "book":"h56ansk4Sabc",
        "rating":3
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

目前支持评论的修改.

目前每个用户对于一本图书只能有一条评论！

修改评论类似，重新发一遍就行。review->contetn 可以为空，发送空字符串就行 !""!.

can not support edit and delet!
request data:

```json
发送评论：
{
    "book_id":"h56ansk4Sabc",
    "review":{
        "content":"2 years later, this still tech me so much! I recommand this book significantly!"
    }
}
空评论也可以：必须要加上空字符串的双引号！！！
{
    "book_id":"h56ansk4Sabc",
    "review":{
        "content":""
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

user_rating_review:
    当前这个用户，也就是登录用户对于当前浏览的书的评分，以及评论内容。

rating_analyse：
    当前浏览的这本书的评分信息。包括平均分，多少人打过分。
    剩下的是每个分数占总评分人数的比例小数，前端需要乘100%并显示。

review_book：
    1.主要优化目标！
    2.这是一个list，每一条评论的信息就是一个object。
    3. 对于每个评论的object：
        id:评论的id.
        content:评论内容.
        user:username.
        book:book id与当前book一致.
        like_count_num：点赞总数.
        create_time：创建时间.
        rating:当前评论所属于的用户对于当前图书的评分.
        like_status：！！！！ 当前浏览网页的登录用户（不是当前这条评论所属于的用户）对于这条评论是否点过赞！如果是这里就是1，不是或者取消了赞，那么就是0！！！ ！！！！！.

your request data:
```
{
    "book_id":"h56ansk4Sabc"
}
```

response:
```json
{
    "id": "zz1ahsqUgXwC",
    "title": "In America",
    "user_rating_review": {
        "user_rating": 3,
        "user_review": "2 years later, this still tech me so much! I recommand this book significantly!"
    },
    "rating_analyse": {
        "how_many_user_scored": 2,
        "average_rating": 4.0,
        "five": 0.5,
        "four": 0.0,
        "three": 0.5,
        "two": 0.0,
        "one": 0.0
    },
    "review_book": [
        {
            "id": 2,
            "content": "gooooooooooooooooooooooooooooood! Interesting!!!!!!",
            "user": "Black",
            "book": "zz1ahsqUgXwC",
            "like_count_num": 0,
            "create_time": "2020-07-23",
            "rating": 5,
            "like_status": 0
        }
    ]
}
```

                                   

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
