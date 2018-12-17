from django.contrib import admin

from .models import *
from .forms import *

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    form = PostForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'date_pub')
    list_filter = ('date_pub',)

    class Media:
        js = (
            '/static/tinymce/jguery.tinymce.min.js',
            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/tiny_mce_init.js',
        )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date_pub', 'text', 'moderation')
    list_filter = ('moderation',)

admin.site.register(Comment, CommentAdmin)
