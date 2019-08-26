from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def index(request):
    data = Post.objects.all()
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    context = {
        'object_list' : data
    }
    return render(request, 'index.html', context)

def single_product(request, id):
    post = get_object_or_404(Post, title=id)
    # post = Post.objects.get(id=id)
    context = {
        'post' : post,
    }
    return render(request, 'project-single.html', context)

def works(request, id):

    news = get_object_or_404(Category, title=id)
    post = Post.objects.filter(categories=news)

    context = {
        'object_list' : post
    }
    return render(request, 'works.html', context)

def introduce(request,id):
    print(id)
    context = {
        'id' : id
    }
    return render(request, 'blog-single.html', context)


