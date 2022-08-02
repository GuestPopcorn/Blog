from django.db import models
from email.mime import image
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=101)
    datetime = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    # Comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True )
    image = models.ImageField(null= True, blank=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100 , null=True)
    Text = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    Post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name='comments')
    def __str__(self) -> str:
        return self.Text

class Tag(models.Model):
    title_tag = models.CharField(max_length=100)
    post = models.ManyToManyField(Post)
    def __str__(self) -> str:
        return self.title_tag
