# Generated by Django 3.2.7 on 2022-01-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clenove', '0004_auto_20220102_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clen',
            name='bobrik',
            field=models.ManyToManyField(null=True, to='clenove.Bobrik'),
        ),
    ]
