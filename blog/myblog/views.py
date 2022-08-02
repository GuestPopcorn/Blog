from django.shortcuts import render

# Create your views here.
def go_post(request):
    return render(request, 'index.html')

def post(request):
    return(render(request, 'index.html'))