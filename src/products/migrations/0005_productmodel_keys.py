# Generated by Django 3.2.4 on 2021-08-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productmodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='keys',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='arama anahtarları'),
        ),
    ]
