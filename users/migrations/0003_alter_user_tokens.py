# Generated by Django 3.2 on 2021-04-30 16:50

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tokens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tokens',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]