from django.shortcuts import render
import products
from products.models import ProductModel 
from haber.models import BlogModel 

def anasayfa(request):
    blogobj = BlogModel.objects.all().order_by('-rating')
    context = {
        'blogobj':blogobj,
    }
    return render(request, "index.html", context)

