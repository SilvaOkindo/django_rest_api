from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.forms import EmailPostForm
from blog.models import Post


# Create your views here.

def home(request):
    return render(request, 'home.html')


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    context = {'post': post}
    return render(request, 'blog/post/detail.html', context=context)


def post_share(request, post_id):
    post = get_object_or_404(Post, id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm()
        if form.is_valid():
            cd = form.cleaned_data
        else:
            form = EmailPostForm()

    return render(
        request,
        'blog/post/share.html',
        {
            'post': post,
            'form': form
        }
    )
