# Generated by Django 4.0.6 on 2022-09-29 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0008_alter_habilidade_projetos'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='capa',
            field=models.ImageField(blank=True, default='', upload_to='projeto/capa/'),
        ),
    ]
