from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def tools(request):
    tools = Tool.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(tools, 4)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'tags': tags,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }

    return render(request, 'worktools/tools.html', context=context)

def tool_detail(request, slug):
    tool = Tool.objects.get(slug__iexact=slug)
    return render(request, 'worktools/tool_detail.html', context={'tool': tool})
