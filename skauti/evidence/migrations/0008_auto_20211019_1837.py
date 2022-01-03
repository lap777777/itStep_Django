# Generated by Django 3.2.7 on 2021-10-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0007_auto_20211019_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bobrik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dovednost', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Bobrici',
            },
        ),
        migrations.AlterModelOptions(
            name='adresa',
            options={'verbose_name_plural': 'Adresy'},
        ),
        migrations.AddField(
            model_name='clen',
            name='bobrik',
            field=models.ManyToManyField(to='evidence.Bobrik'),
        ),
    ]
