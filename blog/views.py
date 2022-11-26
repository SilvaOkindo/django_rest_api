from django.shortcuts import render

from blog.models import Post


# Create your views here.

def home(request):
    return render(request, 'home.html')


def post_list(request):
    posts = Post.published.all()
    context = {'posts': posts}
    return render(request, 'blog/post/list.html', context=context)
