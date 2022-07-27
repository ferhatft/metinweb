from django.db import models
from django.template.defaultfilters import slugify, title

from ckeditor_uploader.fields import RichTextUploadingField




PROJTYPE = (
    ('dijital-baski', 'dijital-baski'),
    ('ankara-display-ürünler', 'ankara-display-ürünler'),
    ('ankara-tabela-sistemleri', 'ankara-tabela-sistemleri'),
    ('ankara-promosyon-ürünleri', 'ankara-promosyon-ürünleri'),
    ('ankara-matbaa-hizmetleri', 'ankara-matbaa-hizmetleri'),
    ('ankara-uv-basi', 'ankara-uv-basi'),
    ('ankara-ankara-web-tasarimi', 'ankara-web-tasarimi'),
)




class ProductModel(models.Model):    
    title                           = models.CharField(max_length=40,verbose_name = "Başlık",blank=True)
    proj_type                       = models.CharField(max_length=50, choices=PROJTYPE, default='dijital-baski',verbose_name='Proje ismi') #
    slug                            = models.SlugField(blank=True , unique=True, max_length=500 ,null=True,verbose_name='uzantı')
    mainimage                       = models.ImageField(verbose_name='resim "569x372"',blank=True, null=True)
    decription                      = RichTextUploadingField(verbose_name="Açıklama",blank=True, null=True)
   
  
    def __str__(self):
        return '%s %s' % (self.title, self.id)

    def save(self, *args, **kwargs):

        title =  slugify(self.title)
        self.slug = title
        

        return super(ProductModel, self).save(*args, **kwargs)
        
    
    def get_absolute_url(self):
        try:
            if self.slug:
                return "/{proj_type}/{slug}/".format(proj_type=self.proj_type.lower().replace(' ','-'),slug=self.slug)
        except:
            return "/projects/{str}".format(str=self.title.lower().replace('-',' '))

    class Meta:
        ordering = ['id']
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'






class ProductModelGaleri(models.Model):
    proj                    = models.ForeignKey(ProductModel, related_name='ProjectModelGaleri', on_delete=models.CASCADE,blank=True, null=True)
    image                   = models.ImageField(upload_to='products-image/', max_length=100,verbose_name='583x430')

    
    def __str__(self):
        return '%s %s' % (self.proj , self.id)

    class Meta:
        ordering = ['id']
        verbose_name = 'galeri '
        verbose_name_plural = 'galeriler'
