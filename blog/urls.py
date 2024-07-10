from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.index, name='index-blog'),
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
]