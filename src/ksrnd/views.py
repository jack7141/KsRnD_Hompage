from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def single_product(request):
    return render(request, 'project-single.html', {})

def works(request):
    return render(request, 'works.html', {})