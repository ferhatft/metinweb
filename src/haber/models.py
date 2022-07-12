from django.db import models

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.,

class BlogModel(models.Model):
    title                   = models.CharField(max_length=500,verbose_name = "başlık", blank=True)
    slug                    = models.SlugField(max_length=500, blank=True, null=True,verbose_name='uzantı')
    image                   = models.ImageField(null=True,verbose_name='ana resim "603-350"')
    rating                  = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True,verbose_name="öne çıkarma")
    created_date            = models.DateField(blank=True, null=True,verbose_name="oluşturulma tarihi")
    intro                   = RichTextUploadingField(blank=True, null=True, verbose_name='içerik') 

    def __str__(self):
        return '%s %s' % (self.title, self.id)

    
    def save(self, *args, **kwargs):
        title =  slugify(self.title)
        self.slug = title

        return super(BlogModel, self).save(*args, **kwargs)

        
    def get_absolute_url(self):
        try:
            if self.slug:
                return "/blog/{str}/".format(str=self.slug)
        except:
            return "/blog/{str}/".format(str=self.title.lower().replace('-',' '))
        
    class Meta:
        ordering = ['title']
        verbose_name = 'blog yazısı'
        verbose_name_plural = 'blog Yazıları'