# Generated by Django 3.1.5 on 2021-02-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lenguajes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lenguaje', models.CharField(max_length=255)),
                ('habilidad', models.IntegerField(max_length=100)),
            ],
            options={
                'verbose_name': 'Lenguaje',
                'verbose_name_plural': 'Lenguajes',
            },
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Experiencia', 'verbose_name_plural': 'Experiencias'},
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='lenguaje',
            new_name='empresa',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='habilidad',
        ),
    ]