# Generated by Django 3.2.4 on 2021-11-11 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20211111_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='price',
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='mainimage',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='resim "569x372"'),
        ),
    ]
