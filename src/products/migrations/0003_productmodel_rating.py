# Generated by Django 3.2.4 on 2021-08-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210805_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, verbose_name='Rating'),
        ),
    ]
