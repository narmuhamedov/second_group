from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogview, name='blog'),
    path('blog/<int:id>/', views.blogdetailview, name='blog_detail'),
]