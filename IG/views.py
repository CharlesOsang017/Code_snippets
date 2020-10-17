from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'IG/home.html', context)


def about(request):
    return render(request, 'IG/about.html', {'title': 'About'})   

