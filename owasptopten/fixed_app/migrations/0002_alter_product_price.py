# Generated by Django 5.1.1 on 2024-10-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixed_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]