# Generated by Django 3.2.7 on 2021-10-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zvire',
            name='barva',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='zvire',
            name='zije',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='zvire',
            name='jmeno',
            field=models.CharField(max_length=30),
        ),
    ]