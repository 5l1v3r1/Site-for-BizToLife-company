from django.urls import path
from .views import *

urlpatterns = [
    path('', blog, name='blog_url'),
    path('<str:slug>/', post_detail, name='post_detail_url'),
]
