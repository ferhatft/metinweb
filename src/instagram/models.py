from django.db import models

class İnstagramModel(models.Model):    
    mainimage                       = models.ImageField(verbose_name='resim "86x76"',blank=True, null=True)
    link                            = models.CharField(max_length=40,verbose_name = "link",blank=True)
  
    def __str__(self):
        return '%s %s' % ('İnstagram feed', self.id)
    

    class Meta:
        ordering = ['id']
        verbose_name = 'İnstagram feed'
        verbose_name_plural = 'İnstagram feed'
