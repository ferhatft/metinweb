# Generated by Django 3.2.4 on 2021-08-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productmodel_keys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='mainimage',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='resim "600x600"'),
        ),
        migrations.AlterField(
            model_name='productmodelgaleri',
            name='image',
            field=models.FileField(upload_to='products-image/', verbose_name='600x600'),
        ),
    ]
