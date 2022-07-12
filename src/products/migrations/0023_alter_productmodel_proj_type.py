# Generated by Django 3.2.4 on 2022-07-12 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_productmodel_proj_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='proj_type',
            field=models.CharField(choices=[('dijital-baski', 'dijital-baski'), ('display-ürünler', 'display-ürünler'), ('tabela-sistemleri', 'tabela-sistemleri'), ('promosyon-ürünleri', 'promosyon-ürünleri'), ('matbaa-hizmetleri', 'matbaa-hizmetleri'), ('ankara-web-tasarimi', 'ankara-web-tasarimi')], default='dijital-baski', max_length=50, verbose_name='Proje ismi'),
        ),
    ]
