from django.shortcuts import get_object_or_404, render

from blog.models import Post, Category


POSTS_ON_MAIN_PAGE = 5


def index(request):
    """
    Функция для отображения главной страницы блога.

    Выводятся пять последних публикаций.
    """
    post_list = Post.posted.all()[:POSTS_ON_MAIN_PAGE]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """
    Функция для отображения подробной информации о посте по идентификатору.

    post_id: идентификатор поста.
    """
    post = get_object_or_404(Post.posted, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """
    Функция для отображения публикаций, принадлежащих к определённой категории.

    category_slug: категория.
    """
    category = get_object_or_404(Category, slug=category_slug,
                                 is_published=True)
    post_list = Post.posted.filter(category=category)
    context = {'category': category,
               'post_list': post_list}
    return render(request, 'blog/category.html', context)
