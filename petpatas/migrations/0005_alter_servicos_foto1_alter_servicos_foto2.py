# Generated by Django 4.1.5 on 2023-02-18 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petpatas', '0004_servicos_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='foto1',
            field=models.ImageField(upload_to='servicosupload/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='foto2',
            field=models.ImageField(upload_to='servicosupload/%Y/%m/%d/'),
        ),
    ]