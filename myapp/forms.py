from django import forms

from .models import List

class PostList(forms.ModelForm):

    class Meta:
        model = List
        fields = ('list_title',)