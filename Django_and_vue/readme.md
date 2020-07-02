
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
Superuser account: username: admin, password: 123456<br>
localhost:8000/admin<br>

Black,123456<br>
Pink,123456<br>
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

## register
```
url: /api/register/
```
1. success, return token
2. error, will return error msg!

## account detail
```
url: /api/account/
```
it will return a json data, which contain the whole info of user except password.

## collection operations
```
url: /api/collection/
```
1.get:
you can acquire the collection set of user

2.post:
you can add a collection with name to user

3.delete:
you can delete a collection with name

>name changing will coming soon……

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
