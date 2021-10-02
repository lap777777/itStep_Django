# Generated by Django 3.2.7 on 2021-10-02 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_branche'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('birth', models.DateField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
