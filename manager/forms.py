# -*- coding: utf-8 -*-
from django import forms

class ScriptlistForm(forms.Form):
    author = forms.CharField(max_length=30)
    tcid = forms.CharField(max_length=30)
    scrfile = forms.FileField(label='Select Input simulator script file(.py)')
    detail = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.Form):

    writer = forms.CharField(max_length=30)
    comments = forms.CharField(widget=forms.Textarea)
