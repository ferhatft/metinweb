from django.conf.urls import url

from django.urls import path

from .views import (
    teklifview,contacview
)

app_name = 'iletisim'

urlpatterns = [
    path('' , contacview, name="iletisim"),   
    path('teklif-al/' , teklifview, name="teklifal"),   
]

