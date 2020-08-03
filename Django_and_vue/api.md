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

>GET search some book with title or authors.

搜索书籍，通过post方法。
请求数据包含搜索类型和搜索关键词
有结果会返回书籍的object的list。
如果没有就返回400.（有待商榷）

```
{
    "search_type": "Title"/"Authors/user",
    "key_word": "python"
}
```


```
{
    "search_type": "user",
    "key_word": "p/pi/pin/pink/Pink"
}
```


return all book objects related to "key_word"
if no result, it will return error msg and status 400.

## search filter
```
url: /api/filter/
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
        "target":2
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

~目前每个用户对于一本图书只能有一条评论!~
现在用户可以进行多次评论了，每条评论都会有用户的评分信息。


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
空评论现在不可以了！！！我在后端已经加了长度限制了。
如果想修改某一条已经发表过的评论：
额外单独添加review id
{
    "book_id":"zz1ahsqUgXwC",
    "review_id":6,
    "review":{
        "content":"5 years later, this book is very interesting! wow!"
    }
}
返回信息为update success！

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

* review_book:
  * 主要优化目标！
  * 这是一个list，每一条评论的信息就是一个object.
  * 对于每个评论的object:
    * id:评论的id.
    * content:评论内容.
    * user:username.
    * book:book id与当前book一致.
    * like_count_num：点赞总数.
    * create_time：创建时间.
    * rating:当前评论所属于的用户对于当前图书的评分.
    * like_status：！！！！ 当前浏览网页的登录用户（不是当前这条评论所属于的用户）对于这条评论是否点过赞！如果是这里就是1，不是或者取消了赞，那么就是0！！！ ！！！！！.

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

#主页简单推荐
```
api/mainpagerec/
```
>GET
返回五本书的信息，

# 推荐页面
```
api/recommend/
```
>GET
这个要发送用户id参数
```
{
    "id":3
}
```

返回值是三个或者两个集合，每个里面都有书
如果是新用户或者用书读过的书太少，不会有用户推荐的书，
```
{
    "rating_rec": [
        {
            "id": "oPIMmQEACAAJ",
            "title": "Harry Potter and the Goblet of Fire",
            "authors": "J. K. Rowling,Mary GrandPré",
            "publisher": "Scholastic Paperbacks",
            "publish_date": "2013-08-27",
            "page_count": 734,
            "avg_rating": "5.0",
            "categories": "Juvenile Fiction",
            "ISBN": 9780545582957,
            "imageLink": "http://books.google.com/books/content?id=oPIMmQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
            "description": "Young wizard-in-training Harry Potter prepares for a competition between Hogwarts School of Magic and two rival schools, develops a crush on Cho Chang, and wishes above all to be a normal fourteen-year-old.",
            "added_times": 1,
            "collection": [
                3
            ]
        },
        {
            "id": "miv82VGPL9cC",
            "title": "The Science of Chocolate",
            "authors": "S. Beckett,Stephen T. Beckett",
            "publisher": "Royal Society of Chemistry",
            "publish_date": "2000",
            "page_count": 175,
            "avg_rating": "5.0",
            "categories": "Cooking",
            "ISBN": 9780854046003,
            "imageLink": "http://books.google.com/books/content?id=miv82VGPL9cC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "description": "Covers the history, ingredients, and processing techniques used in the manufacture of chocolate.",
            "added_times": 1,
            "collection": [
                6
            ]
        },
        {
            "id": "h56ansk4SyQC",
            "title": "Python: A Study of Delphic Myth and Its Origins",
            "authors": "Joseph Eddy Fontenrose",
            "publisher": "Biblo & Tannen Publishers",
            "publish_date": "1974",
            "page_count": 616,
            "avg_rating": "4.2",
            "categories": "Social Science",
            "ISBN": 9780819602855,
            "imageLink": "http://books.google.com/books/content?id=h56ansk4SyQC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "description": "",
            "added_times": 4,
            "collection": [
                1,
                3,
                6,
                7
            ]
        },
        {
            "id": "9SG1r8EJawIC",
            "title": "Numerical Methods in Engineering with Python",
            "authors": "Jaan Kiusalaas",
            "publisher": "Cambridge University Press",
            "publish_date": "2010-01-29",
            "page_count": 422,
            "avg_rating": "4.0",
            "categories": "Technology & Engineering",
            "ISBN": 9781139484152,
            "imageLink": "http://books.google.com/books/content?id=9SG1r8EJawIC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "description": "This text is for engineering students and a reference for practising engineers, especially those who wish to explore Python. This new edition features 18 additional exercises and the addition of rational function interpolation. Brent's method of root finding was replaced by Ridder's method, and the Fletcher-Reeves method of optimization was dropped in favor of the downhill simplex method. Each numerical method is explained in detail, and its shortcomings are pointed out. The examples that follow individual topics fall into two categories: hand computations that illustrate the inner workings of the method and small programs that show how the computer code is utilized in solving a problem. This second edition also includes more robust computer code with each method, which is available on the book website. This code is made simple and easy to understand by avoiding complex bookkeeping schemes, while maintaining the essential features of the method.",
            "added_times": 1,
            "collection": [
                7
            ]
        },
        {
            "id": "vKjWDQAAQBAJ",
            "title": "Django: Web Development with Python",
            "authors": "Samuel Dauzon,Aidas Bendoraitis,Arun Ravindran",
            "publisher": "Packt Publishing Ltd",
            "publish_date": "2016-08-31",
            "page_count": 717,
            "avg_rating": "4.0",
            "categories": "Computers",
            "ISBN": 9781787123922,
            "imageLink": "http://books.google.com/books/content?id=vKjWDQAAQBAJ&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "description": "From an idea to a prototype – a complete guide for web development with the Django framework About This Book Explore the best practices to develop applications of a superior quality with Django framework Unravel the common problems of web development in Django This course teaches you major Django functions and will help you improve your skills by developing models, forms, views, and templates Experience the challenges of working on an end-to-end social network project Who This Book Is For Web developers who want to use modern Python-based web frameworks like Django to build powerful web applications. The course is mostly self-contained and introduces web development with Python to a reader who is familiar with web development concepts and can help him become an expert in this trade. It's intended for all levels of web developers, both students and practitioners from novice to experts. What You Will Learn Use Django models to store information in the database and generate queries to access a database across models Quickly develop web pages to create, read, update, and delete data from the model using class-based views Generate very maintainable forms with Django Import data from local sources and external web services as well as exporting your data to third parties Deep dive into various aspects of Django from models and views to testing and deployment Familiarize yourself with the various nuances of web development such as browser attacks and databases In Detail Data science is hot right now, and the need for multitalented developers is greater than ever before. A basic grounding in building apps with a framework as minimalistic, powerful, and easy-to-learn as Django will be a useful skill to launch your career as an entrepreneur or web developer. Django is a web framework that was designed to strike a balance between rapid web development and high performance. This course will take you on a journey to become an efficient web developer thoroughly understanding the key concepts of Django framework. This learning path is divided into three modules. The course begins with basic concepts of the Django framework. The first module, Django Essentials, is like a practical guide, filled with many real-world examples to build highly effective Django web application. After getting familiar with core concepts of Django, it's time to practice your learning from the first module with the help of over 90 recipes available in this module. In the second module, Web Development with Django Cookbook, you'll learn varying complexities to help you create multilingual, responsive, and scalable websites with Django. By the end of this module, you will have a good understanding of the new features added to Django 1.8 and be an expert at web development processes.The next step is to discover the latest best practices and idioms in this rapidly evolving Django framework. This is what you'll be learning in our third module, Django Design Patterns and Best Practices. This module will teach you common design patterns to develop better Django code. By the end of the module, you will be able to leverage the Django framework to develop a fully functional web application with minimal effort. Style and approach This course includes all the resources that will help you jump into the web development field with Django and learn how to make scalable and robust web applications. The aim is to create a smooth learning path that will teach you how to get started with the powerful Django framework and perform various web development techniques in depth. Through this comprehensive course, you'll learn web development with Django from scratch to finish!",
            "added_times": 1,
            "collection": [
                7
            ]
        }
    ],
    "added_rec": [
        {
            "id": "h56ansk4SyQC",
            "title": "Python: A Study of Delphic Myth and Its Origins",
            "authors": "Joseph Eddy Fontenrose",
            "publisher": "Biblo & Tannen Publishers",
            "publish_date": "1974",
            "page_count": 616,
            "avg_rating": "4.2",
            "categories": "Social Science",
            "ISBN": 9780819602855,
            "imageLink": "http://books.google.com/books/content?id=h56ansk4SyQC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "description": "",
            "added_times": 4,
            "collection": [
                1,
                3,
                6,
                7
            ]
        },
        {
            "id": "yhfdQgq8JF4C",
            "title": "Python Cookbook",
            "authors": "Alex Martelli,David Ascher",
            "publisher": "\"O'Reilly Media, Inc.\"",
            "publish_date": "2002",
            "page_count": 574,
            "avg_rating": "2.5",
            "categories": "Computers",
            "ISBN": 9780596001674,
            "imageLink": "http://books.google.com/books/content?id=yhfdQgq8JF4C&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "description": "Demonstrates the programming language's strength as a Web development tool, covering syntax, data types, built-ins, the Python standard module library, and real world examples.",
            "added_times": 2,
            "collection": [
                1,
                7
            ]
        },
        {
            "id": "9SG1r8EJawIC",
            "title": "Numerical Methods in Engineering with Python",
            "authors": "Jaan Kiusalaas",
            "publisher": "Cambridge University Press",
            "publish_date": "2010-01-29",
            "page_count": 422,
            "avg_rating": "4.0",
            "categories": "Technology & Engineering",
            "ISBN": 9781139484152,
            "imageLink": "http://books.google.com/books/content?id=9SG1r8EJawIC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "description": "This text is for engineering students and a reference for practising engineers, especially those who wish to explore Python. This new edition features 18 additional exercises and the addition of rational function interpolation. Brent's method of root finding was replaced by Ridder's method, and the Fletcher-Reeves method of optimization was dropped in favor of the downhill simplex method. Each numerical method is explained in detail, and its shortcomings are pointed out. The examples that follow individual topics fall into two categories: hand computations that illustrate the inner workings of the method and small programs that show how the computer code is utilized in solving a problem. This second edition also includes more robust computer code with each method, which is available on the book website. This code is made simple and easy to understand by avoiding complex bookkeeping schemes, while maintaining the essential features of the method.",
            "added_times": 1,
            "collection": [
                7
            ]
        },
        {
            "id": "ka2VUBqHiWkC",
            "title": "Effective Java",
            "authors": "Joshua Bloch",
            "publisher": "Addison-Wesley Professional",
            "publish_date": "2008-05-08",
            "page_count": 368,
            "avg_rating": "3.0",
            "categories": "Computers",
            "ISBN": 9780132778046,
            "imageLink": "http://books.google.com/books/content?id=ka2VUBqHiWkC&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api",
            "description": "Are you looking for a deeper understanding of the Java™ programming language so that you can write code that is clearer, more correct, more robust, and more reusable? Look no further! Effective Java™, Second Edition, brings together seventy-eight indispensable programmer’s rules of thumb: working, best-practice solutions for the programming challenges you encounter every day. This highly anticipated new edition of the classic, Jolt Award-winning work has been thoroughly updated to cover Java SE 5 and Java SE 6 features introduced since the first edition. Bloch explores new design patterns and language idioms, showing you how to make the most of features ranging from generics to enums, annotations to autoboxing. Each chapter in the book consists of several “items” presented in the form of a short, standalone essay that provides specific advice, insight into Java platform subtleties, and outstanding code examples. The comprehensive descriptions and explanations for each item illuminate what to do, what not to do, and why. Highlights include: New coverage of generics, enums, annotations, autoboxing, the for-each loop, varargs, concurrency utilities, and much more Updated techniques and best practices on classic topics, including objects, classes, libraries, methods, and serialization How to avoid the traps and pitfalls of commonly misunderstood subtleties of the language Focus on the language and its most fundamental libraries: java.lang, java.util, and, to a lesser extent, java.util.concurrent and java.io Simply put, Effective Java™, Second Edition, presents the most practical, authoritative guidelines available for writing efficient, well-designed programs.",
            "added_times": 1,
            "collection": []
        },
        {
            "id": "oPIMmQEACAAJ",
            "title": "Harry Potter and the Goblet of Fire",
            "authors": "J. K. Rowling,Mary GrandPré",
            "publisher": "Scholastic Paperbacks",
            "publish_date": "2013-08-27",
            "page_count": 734,
            "avg_rating": "5.0",
            "categories": "Juvenile Fiction",
            "ISBN": 9780545582957,
            "imageLink": "http://books.google.com/books/content?id=oPIMmQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
            "description": "Young wizard-in-training Harry Potter prepares for a competition between Hogwarts School of Magic and two rival schools, develops a crush on Cho Chang, and wishes above all to be a normal fourteen-year-old.",
            "added_times": 1,
            "collection": [
                3
            ]
        }
    ]
}
```

                                   
