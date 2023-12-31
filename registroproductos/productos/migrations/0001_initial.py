# Generated by Django 4.1.7 on 2023-11-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='productos_imagenes/')),
            ],
        ),
    ]
