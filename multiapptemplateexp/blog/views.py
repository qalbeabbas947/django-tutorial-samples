from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'name': 'John Doe',
        'age': 30,
        'skills': ['Python', 'Django', 'JavaScript'],
        'user': User('John Doe', 30),
        'blog': {
            'title': 'My Blog',
            'content': '<b>This is my personal blog.</b>',
            'created_at': datetime(2024, 6, 1, 12, 0, 0),
        },
        'empty_value': None,
    }

    return render(request, 'blog/home.html', context)

def blog_details(request):
    context = {
            'title': 'My Blog',
            'description': '<b>This is my personal blog.</b>',
            'author': None,
            'created_at': datetime(2024, 6, 1, 12, 0, 0),
            'price': 5990.234,
            'tags': ['Python', 'Django', 'Web Development'],
        }
    
    return render(request, 'blog/blog_details.html', context)

def control_structures(request):
    blogs = [
        {'title': 'Blog 1', 'is_featured': True, 'author': 'John Doe'},
        {'title': 'Blog 2', 'is_featured': False, 'author': 'Jane Smith'},
        {'title': 'Blog 3', 'is_featured': True, 'author': None},

    ]
    context = {
        'blogs': blogs,
        'today': datetime.now(),
        'html_code': '<b>This is bold text.</b>',
    }
    return render(request, 'blog/control_structures.html', context)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        