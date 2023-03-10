from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def blogview(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


def blogdetailview(request, id):
    post_detail = get_object_or_404(models.Post, id=id)
    return render(request, 'post_list_detail.html', {'post_detail': post_detail})

#create post
def create_post_view(request):
    method = request.method
    form = forms.ShowForm
    if method == "POST":
        form = forms.ShowForm(request.POST, request.FILES)
        form.save()
        return HttpResponse('Фильм успешно добавлен!')
    else:
        form = forms.ShowForm()

    return render(request, 'add_show.html', {'form':form})