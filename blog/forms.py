# -*- coding: utf-8 -*-
from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'name', 'text',}

    def save(self):
        new_comment = Comment.objects.create(
            name = self.cleaned_data['name'],
            text = self.cleaned_data['text']
        )
        return new_comment
