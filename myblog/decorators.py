
from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps

def register_qilmagan(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else :
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=()):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
                
            else :
                return HttpResponse('sizda huquq yo\'q')

        return wrapper_func
    return decorator