from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    data={
        'categoryData': Category.objects.all(),
        'newsData': Post.objects.all(),
    }
    return render(request, 'pages/home/index.html', data)

def about(request):
    return render(request, 'pages/about/index.html')

def contact(request):
    return render(request, 'pages/contact/index.html')

def news(request):
    list_Data = Post.objects.all()
    paginator = Paginator(list_Data, 6)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data={
        'newsData': page_obj
    }
    return render(request, 'pages/news/index.html', data)

def category_view(request, slug):
    data={
        'categoryData': Category.objects.get(slug=slug),
    }
    return render(request, 'pages/news/category.html', data)



def details(request, slug):
    obj = Post.objects.get(slug=slug)
    obj.page_views +=1
    obj.save()
    datta={
        'newsData': Post.objects.get(slug=slug)
    }
    return render(request, 'pages/news/details.html', datta)