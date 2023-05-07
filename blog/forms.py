from django import forms

from .models import POST

class PostForm(forms.ModelForm):

    class Meta:
        model = POST
        fields = ('title', 'text',)