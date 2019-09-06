from django.shortcuts import render, get_object_or_404

from django.views import generic

from .models import Post
# Create your views here.


class IndexView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(published=True)


def detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})
