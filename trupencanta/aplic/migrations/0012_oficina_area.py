# Generated by Django 4.2.8 on 2023-12-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0011_alter_oficina_descricao_alter_oficina_resumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='oficina',
            name='area',
            field=models.TextField(default=1, help_text='Insira a área da oficina, como Artes cênicas, canto', verbose_name='Área da Oficina'),
            preserve_default=False,
        ),
    ]
