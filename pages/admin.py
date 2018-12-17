from django.contrib import admin

from .models import *
from .forms import *

# Register your models here.
@admin.register(EventTime)
class EventTimeModelAdmin(admin.ModelAdmin):
    form = EventTimeForm
    list_display = ('time_to_start_event', 'title', 'disc',)
