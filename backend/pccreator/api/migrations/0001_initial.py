# Generated by Django 3.0.6 on 2020-05-10 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del PC')),
                ('budget', models.IntegerField(blank=True, null=True, verbose_name='Presupueto')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PC',
                'verbose_name_plural': 'PCs',
            },
        ),
    ]
