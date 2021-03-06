# Generated by Django 3.2 on 2021-05-01 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_tokens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='tokens',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.token'),
        ),
    ]
