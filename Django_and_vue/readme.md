
# Require
1.install virtual env
```
sudo pip3 install virtualenv
```
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

# account(username and password)
Black,123456<br>
Pink,123456<br>
you can create new account, do not use complex password, if account create success, password will be Encrypted! you can not check it by /admin!

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
└── readbook
    ├── account
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   ├── admin.cpython-37.pyc
    │   │   ├── apps.cpython-37.pyc
    │   │   ├── models.cpython-37.pyc
    │   │   └── urls.cpython-37.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_auto_20200625_0554.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-37.pyc
    │   │       ├── 0002_auto_20200625_0554.cpython-37.pyc
    │   │       └── __init__.cpython-37.pyc
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── backed
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   ├── admin.cpython-37.pyc
    │   │   ├── apps.cpython-37.pyc
    │   │   ├── models.cpython-37.pyc
    │   │   ├── serializers.cpython-37.pyc
    │   │   ├── urls.cpython-37.pyc
    │   │   └── views.cpython-37.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-37.pyc
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
        │   ├── __init__.cpython-37.pyc
        │   ├── settings.cpython-37.pyc
        │   ├── urls.cpython-37.pyc
        │   └── wsgi.cpython-37.pyc
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```
