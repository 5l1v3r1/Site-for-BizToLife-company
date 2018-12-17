from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
@admin.register(Tool)
class ToolModelAdmin(admin.ModelAdmin):
    form = ToolForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'disc', 'slug', 'date_pub',)
    list_filter = ('date_pub',)
    filter_horizontal = ('tag',)

    class Media:
        js = (
            '/static/tinymce/jguery.tinymce.min.js',
            '/static/tinymce/tinymce.min.js',
            '/static/tinymce/tiny_mce_init.js',
        )

@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    form = TagForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'posts',)
