# Generated by Django 3.2.7 on 2021-10-19 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0005_auto_20211019_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oddil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=30)),
                ('vlajka', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='clen',
            name='oddil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evidence.oddil'),
        ),
    ]
