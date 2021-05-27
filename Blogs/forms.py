from django import forms
from django.db.models import fields
from .models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['Title','Text']
        labels = {'Text':'Text','Title':'Tittle'}
        widgets = {'Text': forms.Textarea(attrs={'cols':80}),'Title': forms.Textarea(attrs={'cols':40,'rows':2})}

        