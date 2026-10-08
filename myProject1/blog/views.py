from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #return render(request, 'blog/home.html', {'title': 'Home'})
    return HttpResponse("Blog Home Page")

def about(request):
    #return render(request, 'blog/home.html', {'title': 'Home'})
    return HttpResponse("Blog about Page")

def post_details(request, post_id):
    return HttpResponse(f"<h1>Post Detail Page for Post ID: {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>User Profile Page for Username: {username}</h1>")


def kwargs_show(request, **kwargs):
    return HttpResponse(f"<h1>User Profile Page for Username: {kwargs.get('username')} {kwargs}</h1>")