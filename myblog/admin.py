from django.contrib import admin
from .models import Category, Comment, Post, Tag
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)