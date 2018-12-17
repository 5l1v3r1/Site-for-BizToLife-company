# -*- coding: utf-8 -*-
from django import forms
from .models import *

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        exclude = []

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = []
