# Generated by Django 3.2.4 on 2022-07-12 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20220712_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True, verbose_name='uzantı'),
        ),
    ]