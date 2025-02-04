# Generated by Django 3.2.4 on 2021-11-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(blank=True, null=True, upload_to='', verbose_name='resim "86x76"')),
                ('link', models.CharField(blank=True, max_length=40, verbose_name='link')),
            ],
            options={
                'verbose_name': 'İnstagram feed',
                'verbose_name_plural': 'İnstagram feed',
                'ordering': ['id'],
            },
        ),
    ]
