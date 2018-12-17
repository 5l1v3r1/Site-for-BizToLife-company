from django.shortcuts import render
from .models import *

# Create your views here.
def comming_soon(request):
    data = EventTime.objects.get(pk=1)
    return render(request, 'pages/comming_soon.html', context={'data':data})

def faq_page(request):
    return render(request, 'pages/faq.html')

def selection_page(request):
    return render(request, 'pages/selection.html')

def about_us_page(request):
    return render(request, 'pages/about.html')
