from django.shortcuts import render
from .models import *
from .forms import CommentForm
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)

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
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }

    return render(request, 'blog/post_list.html', context=context)

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    comment = Comment.objects.all().filter(post=post, moderation=True)
    form = Comment()
    if request.method == 'POST':
        name = request.POST.get('name')
        text = request.POST.get('text')
        form.name=name
        form.text=text
        form.post=post
        form.created_date = timezone.now()
        form.save()
        return redirect(post)

    return render(request, 'blog/post_detail.html', context={
                                                    'post': post,
                                                    'comments': comment
                                                    })
