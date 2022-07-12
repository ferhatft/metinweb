from django.urls import path, include
from .views import blog,blogdetay

urlpatterns = [
    path('', blog, name="blog"),
    path('<slug:slug>/', blogdetay, name="blogdetay"),
    
]
