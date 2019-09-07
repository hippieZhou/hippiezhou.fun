from django.shortcuts import render, get_object_or_404

from django.views import generic

from .models import ArticlePost
# Create your views here.


class IndexView(generic.ListView):
    model = ArticlePost
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return ArticlePost.objects.filter(published=True).order_by('-created')


def detail(request, id, slug):
    post = get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})
