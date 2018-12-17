# -*- coding: utf-8 -*-
from django import forms
from .models import *

class EventTimeForm(forms.ModelForm):
    class Meta:
        model = EventTime
        exclude = []

    #ACCEPTABLE_FORMATS = ['%Y-%m-%d %H:%M']
    #time_to_start_event = forms.DateTimeField(input_formats=ACCEPTABLE_FORMATS)
