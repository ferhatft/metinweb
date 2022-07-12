from django.shortcuts import render, get_object_or_404
from .models import BlogModel
from django.db.models import Q




def blog(request):

    blogs = BlogModel.objects.all().order_by('-id')

    context = {
        'blogs':blogs,
    }

    return render(request, 'blog.html', context)

    
def blogdetay(request, slug):

    allblogs = BlogModel.objects.all()[:4]

    obj = get_object_or_404(BlogModel, slug=slug)

    context = {
        'allblogs':allblogs,
        'obj': obj,
    }

    return render(request, 'blogdetay.html', context)