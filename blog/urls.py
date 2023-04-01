from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("blog/<int:id>/", views.PostDetailView.as_view(), name="blog_detail"),
    path("blog/<int:id>/update/", views.BlogUpdateView.as_view(), name='update'),
    path("blog/<int:id>/delete/", views.BlogDeleteView.as_view(), name='delete'),
    path("add-tvshow/", views.BlogCreateView.as_view(), name="create"),
    path("search/", views.Search.as_view(), name='search'),
]
