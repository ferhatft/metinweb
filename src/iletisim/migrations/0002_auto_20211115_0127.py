# Generated by Django 3.2.4 on 2021-11-14 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
