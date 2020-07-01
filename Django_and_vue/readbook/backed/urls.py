from django.urls import path
from rest_framework import routers
from django.conf.urls import url

from rest_framework.authtoken import views
from .views import *

app_name='backed'
urlpatterns=[
    # url('login/', views.obtain_auth_token),
    url('login/', CustomAuthToken.as_view()),
    url('register/', RegisterAPIView.as_view()),
    url('account/', AccountDetailAPIView.as_view()),
    url('collection/', CreateCollectionAPIView.as_view()),
    url('add_book/', AddBookAPIView.as_view()),
]