# Generated by Django 3.2.7 on 2021-10-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clen',
            name='vek',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clen',
            name='prispevek',
            field=models.BooleanField(null=True),
        ),
    ]
