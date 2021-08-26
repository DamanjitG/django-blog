from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'This is some content for the first post',
        'date_posted': 'Aug 25 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is some content for the second post',
        'date_posted': 'Jan 1 2009'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})