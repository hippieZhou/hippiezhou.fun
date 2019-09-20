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
        return Post.published.order_by('-created')


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status=True,
                             publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/detail.html', {'post': post})
