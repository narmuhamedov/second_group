from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class BlogView(generic.ListView):
    template_name = 'post_list.html'
    queryset = models.Post.objects.all()

    def get_queryset(self):
        return models.Post.objects.all()

# def blogview(request):
#     post = models.Post.objects.all()
#     return render(request, "post_list.html", {"post": post})


class PostDetailView(generic.DetailView):
    template_name = 'post_list_detail.html'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=blog_id)

# def blogdetailview(request, id):
#     post_detail = get_object_or_404(models.Post, id=id)
#     return render(request, "post_list_detail.html", {"post_detail": post_detail})
#

# create
class BlogCreateView(generic.CreateView):
    template_name = 'add-tvshow.html'
    form_class = forms.TvShowForm
    queryset = models.Post.objects.all()
    success_url = "/blog/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BlogCreateView, self).form_valid(form=form)

# def create_tvshow_view(request):
#     method = request.method
#     if method == "POST":
#         form = forms.TvShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Фильм успешно добавлен!")
#     else:
#         form = forms.TvShowForm()
#     return render(request, "add-tvshow.html", {"form": form})

#update
class BlogUpdateView(generic.UpdateView):
    template_name = 'updateblog.html'
    form_class = forms.TvShowForm
    success_url = '/blog/'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=blog_id)

    def form_valid(self, form):
        return super(BlogUpdateView, self).form_valid(form=form)

# def tvshoupdateview(request, id):
#     blog_object = get_object_or_404(models.Post, id=id)
#     if request.method == 'POST':
#         form = forms.TvShowForm(instance=blog_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Блог успешно обновлен')
#
#     else:
#         form = forms.TvShowForm(instance=blog_object)
#     return render(request, 'updateblog.html', {"form": form,
#                                                "object": blog_object
#                                                })

#delete
class BlogDeleteView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/blog/'

    def get_object(self, **kwargs):
        blog_id = self.kwargs.get('id')
        return get_object_or_404(models.Post, id=blog_id)
# def deleteblogvie2w(request, id):
#     blog_object = get_object_or_404(models.Post, id=id)
#     blog_object.delete()
#     return HttpResponse('Блог успешно удален')


#Кнопка поиска
class Search(generic.ListView):
    template_name = 'post_list.html'
    context_object_name = 'blog'
    paginate_by = 5

    def get_queryset(self):
        return models.Post.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context