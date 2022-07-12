from django.shortcuts import render,redirect,reverse

from django.db.models import Q

from .models import ProductModel
# Create your views here.


def ankara_dijital_baski(request):
    projects = ProductModel.objects.filter(proj_type='dijital-baski')
    
    context = {
        'title':'Ankara Dijital Baskı',

        'projects':projects,

    }
    return render(request, "ankara_dijital_baski.html", context)
def ankara_display_urunleri(request):
    projects = ProductModel.objects.filter(proj_type='ankara-display-ürünler')
    
    context = {
        'title':'Ankara Display Ürünler',

        'projects':projects,

    }
    return render(request, "ankara_display_urunleri.html", context)
def ankara_tabela_sistemleri(request):
    projects = ProductModel.objects.filter(proj_type='ankara-tabela-sistemleri')
    
    context = {
        'title':'Ankara Tabela Sistemleri',

        'projects':projects,

    }
    return render(request, "ankara_tabela_sistemleri.html", context)
def  ankara_promosyon_urunleri(request):
    projects = ProductModel.objects.filter(proj_type='ankara-promosyon-ürünleri')
    
    context = {
        'title':'Ankara Promosyon Ürünleri',

        'projects':projects,

    }
    return render(request, "ankara_promosyon_urunleri.html", context)
def ankara_matbaa_hizmetleri(request):
    projects = ProductModel.objects.filter(proj_type='ankara-matbaa-hizmetleri')
    
    context = {
        'title':'Ankara Matba Hizmetleri',

        'projects':projects,

    }
    return render(request, "ankara_matbaa_hizmetleri.html", context)

def ankara_web_tasarimi(request):
    projects = ProductModel.objects.filter(proj_type='ankara-ankara-web-tasarimi')
    
    context = {
        'title':'Ankara Web Tasarimi',

        'projects':projects,

    }
    return render(request, "ankara_web_tasarimi.html", context)




def productdetail(request,slug,proj_type): 
    

    projects = ProductModel.objects.filter(proj_type=proj_type)
    obj = ProductModel.objects.filter(slug=slug).first()

    print("-------------------------")

    
    print(slug)
    print(proj_type)
    print(projects)
    print(obj)

    context = {
        'projects':projects,
        'obj':obj,

    }
    return render(request, "project_galeri.html", context)

