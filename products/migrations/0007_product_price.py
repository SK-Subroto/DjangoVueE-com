# Generated by Django 3.2 on 2021-05-08 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210506_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]