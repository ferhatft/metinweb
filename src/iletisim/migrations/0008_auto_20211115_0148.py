# Generated by Django 3.2.4 on 2021-11-14 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0007_alter_teklif_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teklif',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='teklif',
            name='uyer',
            field=models.CharField(blank=True, choices=[('instagram', 'İnstagram'), ('twitter', 'Twitter'), ('facebook', 'Facebook')], max_length=60, null=True),
        ),
    ]