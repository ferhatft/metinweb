from django.shortcuts import render,redirect
from instagram.models import İnstagramModel

def add_variable_to_context(request):
    insobj = İnstagramModel.objects.all()[:6]
    
    return {
        'insobj':insobj,
    }
