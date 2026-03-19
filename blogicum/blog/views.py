from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post, Category


def index(request):
    """
    Функция для отображения главной страницы блога.

    Выводятся пять последних публикаций.
    """
    post_list = Post.objects.all().filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """
    Функция для отображения подробной информации о посте по идентификатору.

    post_id: идентификатор поста.
    """
    post = get_object_or_404(Post.objects.filter(
        Q(pub_date__lte=timezone.now())
        & Q(is_published=True)
        & Q(category__is_published=True)
    ), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """
    Функция для отображения публикаций, принадлежащих к определённой категории.

    category_slug: категория.
    """
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = Post.objects.all().filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {'category': category,
               'post_list': post_list}
    return render(request, 'blog/category.html', context)
