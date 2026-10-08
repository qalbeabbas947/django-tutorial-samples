from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    # path('post/<int:post_id>/', views.post_details, name='blog-post-detail'),
    path('user/<str:username>/', views.user_profile, name='blog-user-profile'),
    re_path(r'^post/(?P<post_id>\d+)/$', views.post_details, name='blog-post-detail-regex'),
    path('kwargs/<str:year>/<str:month>/<str:day>/', views.kwargs_show, name='blog-kwargs-show'),
    
]