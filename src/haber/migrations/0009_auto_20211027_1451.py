# Generated by Django 3.1 on 2021-10-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0008_blogmodel_bg_color_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image_tree',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='gift-image "511x475"'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='image_two',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='gift-image "356x475"'),
        ),
    ]