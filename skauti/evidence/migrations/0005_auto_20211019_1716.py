# Generated by Django 3.2.7 on 2021-10-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0004_alter_clen_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clen',
            name='id',
        ),
        migrations.AlterField(
            model_name='clen',
            name='slug',
            field=models.SlugField(blank='True', default='', primary_key=True, serialize=False),
        ),
    ]
