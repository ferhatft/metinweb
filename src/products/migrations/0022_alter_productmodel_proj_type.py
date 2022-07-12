# Generated by Django 3.2.4 on 2022-07-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_productmodel_proj_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='proj_type',
            field=models.CharField(choices=[('dijital-baski', 'dijital-baski'), ('display-ürünler', 'Display Ürünler'), ('tabela-sistemleri', 'Tabela Sistemleri'), ('promosyon-ürünleri', 'Promosyon Ürünleri'), ('matbaa-hizmetleri', 'Matbaa Hizmetleri'), ('ankara-web-tasarimi', 'Ankara Web Tasarımı')], default='dijital-baski', max_length=50, verbose_name='Proje ismi'),
        ),
    ]
