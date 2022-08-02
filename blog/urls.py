"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atexit import register
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import logoutPage
from main.views import about_me, contact_me, post_update,post_delete, loginPage, home_page, home_page2, post_detail, registerPage,comment_new, add_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),    
    path('contact', contact_me),
    path('about', about_me),
    path('home', home_page2, name='home'),
    path('login', loginPage, name='login'),
    path('comment/new', comment_new, name='comment_new'),
    path('post/add', add_post, name='add_post'),
    path('post/update/<str:pk>', post_update, name='post_update'),
    path('post/delete/<str:pk>', post_delete, name='post_delete'),
    path('post/<str:pk>', post_detail, name='post_detail'),
    path('register', registerPage , name='register'),
    path('logout', logoutPage ,  name='logout'),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
