# Generated by Django 5.0.1 on 2024-01-13 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0002_ticket_categoría'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='eventos')),
            ],
        ),
    ]
