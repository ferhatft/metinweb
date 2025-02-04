# Generated by Django 3.2.4 on 2021-11-11 06:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20211111_0952'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodelgaleri',
            options={'ordering': ['id'], 'verbose_name': 'galeri ', 'verbose_name_plural': 'galeriler'},
        ),
        migrations.RenameField(
            model_name='productmodelgaleri',
            old_name='drinks',
            new_name='proj',
        ),
        migrations.RemoveField(
            model_name='productmodelgaleri',
            name='created_date',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='included',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='dahil olanlar'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='not_included',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='dahil olmayanlar'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='project_detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='proje detayı'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='project_doc',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='proje dosyası'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='title',
            field=models.CharField(blank=True, max_length=40, verbose_name='proje kodu'),
        ),
        migrations.AlterField(
            model_name='productmodelgaleri',
            name='image',
            field=models.FileField(upload_to='products-image/', verbose_name='583x430'),
        ),
    ]
