# Generated by Django 3.1.3 on 2020-11-12 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('celular', models.CharField(max_length=12)),
                ('contraseña', models.CharField(max_length=20)),
            ],
            options={
                'permissions': (('administrador', 'Es administrador'), ('cliente', 'Es cliente')),
            },
        ),
    ]
