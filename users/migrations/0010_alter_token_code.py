# Generated by Django 3.2 on 2021-05-01 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210501_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
