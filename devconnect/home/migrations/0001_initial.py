# Generated by Django 5.1.3 on 2024-12-04 00:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('web', 'web'), ('movil', 'movil'), ('escritorio', 'escritorio'), ('data science', 'data science'), ('machine learning', 'machine learning'), ('otros', 'otros')], max_length=100)),
                ('descripcion', models.TextField()),
                ('tiempo', models.CharField(choices=[('1 semana', '1 semana'), ('2 semanas', '2 semanas'), ('3 semanas', '3 semanas'), ('1 mes', '1 mes'), ('2 meses', '2 meses'), ('3 meses', '3 meses'), ('mas de 3 meses', 'mas de 3 meses'), ('obra labor', 'obra labor')], max_length=100)),
                ('sueldo', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_finalizacion', models.DateTimeField()),
                ('estado', models.CharField(choices=[('en espera', 'en espera'), ('en progreso', 'en progreso'), ('finalizado', 'finalizado')], max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('freelancer_asignado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer_asignado', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
