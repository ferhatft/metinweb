# Generated by Django 3.2.4 on 2021-11-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0005_teklif'),
    ]

    operations = [
        migrations.AddField(
            model_name='teklif',
            name='uyer',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
