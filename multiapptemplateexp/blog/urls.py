from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_details', views.blog_details, name='blog-details'),
    path('control_structures', views.control_structures, name='control-structures'),
    
]