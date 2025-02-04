# Generated by Django 3.2.4 on 2021-11-14 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_productmodel_proj_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='proj_code',
            field=models.CharField(blank=True, max_length=40, verbose_name='proje kodu'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='proj_type',
            field=models.CharField(blank=True, max_length=40, verbose_name='proje türü'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='title',
            field=models.CharField(blank=True, max_length=40, verbose_name='Başlık'),
        ),
    ]
