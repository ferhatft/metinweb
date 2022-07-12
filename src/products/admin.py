from django.contrib import admin

from .models import ProductModel,ProductModelGaleri
# Register your models here.

admin.site.register(ProductModelGaleri)


class ProductModelGaleriAdmin(admin.TabularInline):
    model = ProductModelGaleri
    extra = 1


class SanayiModelAdmin(admin.ModelAdmin):

    inlines = (ProductModelGaleriAdmin,)

    # fields = ('title', 'tags','slug','author','backimage','rating','created_date' , 'intro','anahaber',)

    # readonly_fields = ('rating','created_date')

    # list_display = ('title', 'rating', 'author',)

    # list_filter = ('created_date', 'rating',)

    # ordering = ('-created_date',)


admin.site.register(ProductModel, SanayiModelAdmin)