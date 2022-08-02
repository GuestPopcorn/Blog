from django.shortcuts import render
from myblog.models import Post
# Create your views here.
def home_page(request):
    data = Post.objects.all() #select * from Post
    context = {'data': data}
    return render(request, 'index.html', context=context)

def home_page2(request):
    data = Post.objects.all() #select * from Post
    context = {'data': data}
    return render(request, 'index.html', context=context)

def go_post(request):
    return render(request, 'post.html')

def about_me(request):
    return render(request, 'about.html')

def contact_me(request):
    return render(request, 'contact.html')