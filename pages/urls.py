from django.urls import path
from .views import *

urlpatterns = [
    path('coming_soon/', comming_soon, name='coming_soon_url'),
    path('faq/', faq_page, name='faq_page_url'),
    path('selection/', selection_page, name='selection_page_url'),
    path('about/', about_us_page, name='about_url'),
]
