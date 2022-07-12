# Generated by Django 3.2.4 on 2022-07-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_alter_productmodel_proj_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='proj_type',
            field=models.CharField(choices=[('dijital-baski', 'dijital-baski'), ('ankara-display-ürünler', 'ankara-display-ürünler'), ('ankara-tabela-sistemleri', 'ankara-tabela-sistemleri'), ('ankara-promosyon-ürünleri', 'ankara-promosyon-ürünleri'), ('ankara-matbaa-hizmetleri', 'ankara-matbaa-hizmetleri'), ('ankara-ankara-web-tasarimi', 'ankara-web-tasarimi')], default='dijital-baski', max_length=50, verbose_name='Proje ismi'),
        ),
    ]
