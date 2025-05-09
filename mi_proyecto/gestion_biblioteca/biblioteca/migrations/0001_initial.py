# Generated by Django 5.2.1 on 2025-05-07 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('biografia', models.TextField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('fecha_publicacion', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='biblioteca.autor')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('usuario', models.CharField(max_length=200)),
                ('estado', models.CharField(choices=[('Prestado', 'Prestado'), ('Devuelto', 'Devuelto')], default='Prestado', max_length=50)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos', to='biblioteca.libro')),
            ],
        ),
    ]
