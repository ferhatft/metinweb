# Generated by Django 3.2.4 on 2021-11-14 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_productmodel_proj_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodelgaleri',
            name='proj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ProjectModelGaleri', to='products.productmodel'),
        ),
    ]