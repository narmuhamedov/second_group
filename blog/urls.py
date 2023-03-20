from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.blogview, name="blog"),
    path("blog/<int:id>/", views.blogdetailview, name="blog_detail"),
    path("blog/<int:id>/update/", views.tvshoupdateview, name='update'),
    path("blog/<int:id>/delete/", views.deleteblogview, name='delete'),
    path("add-tvshow/", views.create_tvshow_view, name="create"),
]
