from dataclasses import field
from pyexpat import model
from django import forms
from myblog.models import Comment, Post


class PostCreateForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['auther','title', 'content', 'category']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['Text', 'Post']