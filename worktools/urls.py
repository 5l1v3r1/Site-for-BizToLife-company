from django.urls import path
from .views import *

urlpatterns = [
    path('', tools, name='tools_url'),
    path('<str:slug>/', tool_detail, name='tool_detail_url'),
]
