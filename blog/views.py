from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def blogview(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})


def blogdetailview(request, id):
    post_detail = get_object_or_404(models.Post, id=id)
    return render(request, 'post_list_detail.html', {'post_detail': post_detail})

#create
def create_tvshow_view(request):
    method = request.method
    if method == "POST":
        form = forms.TvShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Фильм успешно добавлен!")
    else:
        form = forms.TvShowForm()
    return render(request, 'add-tvshow.html', {'form': form})