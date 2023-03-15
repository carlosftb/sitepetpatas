# Generated by Django 4.1.5 on 2023-02-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_cliente_senha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='senha',
            new_name='password',
        ),
        migrations.AddField(
            model_name='cliente',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
