# Generated by Django 3.1.5 on 2021-02-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenguaje', models.CharField(max_length=255)),
                ('tiempo', models.IntegerField(max_length=10)),
                ('habilidad', models.IntegerField(max_length=100)),
            ],
        ),
    ]
