from multiprocessing import context
from django.shortcuts import redirect, render
from myblog.decorators import allowed_users, register_qilmagan
from myblog.forms import CommentCreateForm, PostCreateForms
from myblog.models import Comment, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home_page(request):
    data = Post.objects.all() #select * from Post
    context = {'data': data}
    return render(request, 'index.html', context=context)

def home_page2(request):
    data = Post.objects.all() #select * from Post
    context = {'data': data}
    return render(request, 'index.html', context=context)

def post_detail(request, pk):
    data = Post.objects.get(id=pk)
    data.view_count = data.view_count+1
    data.save()
    comments = Comment.objects.order_by('-id').all()
    context = {'post': data, 'comments': comments}
    return render(request, 'post.html', context=context)

def comment_new(request):
    print('comment new')
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('post_detail', comment.Post.id )
        else:
            print(form.errors)
    form = PostCreateForms()
    context = {'form': form}
    print(request.POST)
    return render(request, 'add_post.html', context)\

def add_post(request):
    if request.method == 'POST':
        form = PostCreateForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request,"Успешно добавлен!")
            return redirect('post_detail', post.id )
        else:
            messages.warning(request, form.errors)
            print(form.errors)    
    form = PostCreateForms()
    context = {'form': form}
    return render(request, 'add_post.html', context)

def about_me(request):
    return render(request, 'about.html')
 
def contact_me(request):
    return render(request, 'contact.html')

@register_qilmagan
def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
        else:
            messages.error(request, form.errors)
            # print(form.errors)
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registerPage.html', context)

@register_qilmagan
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password incorrect')
            return redirect('login')

    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

def post_update(request, pk):
    post = Post.objects.get(id=pk)
    form = PostCreateForms(instance=post)
    if request.method == 'POST':
        form = PostCreateForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Muvafaqqiyatli o'zgartirildi")
            return redirect('post_detail', post.id)
        else:
            messages.warning(request, form.errors)
            print(form.errors)
    context = {'form': form}
    return render(request, 'add_post.html', context)

@allowed_users(allowed_roles=['manager'])
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    # post.status = inactive
    post.delete()
    messages.error(request, 'Maqola o\'chirildi')
    return redirect('home')