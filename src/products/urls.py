from django.urls import path

from .views import productdetail, projects_tek,ankara_dijital_baski,ankara_web_tasarimi, ankara_display_urunleri ,ankara_tabela_sistemleri , ankara_promosyon_urunleri , ankara_matbaa_hizmetleri,ankara_matbaa_hizmetleri,ankara_web_tasarimi,productdetail


urlpatterns = [
    path('', projects_tek, name="projects"),
    path('ankara-dijital-baski/', ankara_dijital_baski, name="ankara_dijital_baski"),
    path('ankara-display-urunleri', ankara_display_urunleri , name="ankara_display_urunleri"),
    path('ankara-tabela-sistemleri', ankara_tabela_sistemleri, name="ankara_tabela_sistemleri"),
    path('ankara-promosyon-urunleri', ankara_promosyon_urunleri , name="ankara_promosyon_urunleri"),
    path('ankara-matbaa-hizmetleri', ankara_matbaa_hizmetleri, name="ankara_matbaa_hizmetleri"),
    path('ankara-web-tasarimi', ankara_web_tasarimi, name="ankara_web_tasarimi"),
    path('<slug:proj_type>/<slug:slug>/', productdetail, name="productdetail"),

]