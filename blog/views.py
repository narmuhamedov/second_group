from django.shortcuts import render, get_object_or_404
from . import models

def blogview(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


def blogdetailview(request, id):
    post_detail = get_object_or_404(models.Post, id=id)
    return render(request, 'post_list_detail.html', {'post_detail': post_detail})
