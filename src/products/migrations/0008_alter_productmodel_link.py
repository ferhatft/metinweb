# Generated by Django 3.2.4 on 2021-08-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productmodel_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='link',
            field=models.CharField(blank=True, max_length=400000, verbose_name='satın alma linki'),
        ),
    ]
