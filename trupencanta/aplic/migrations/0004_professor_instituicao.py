# Generated by Django 4.2.8 on 2023-12-17 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='instituicao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aplic.instituicao'),
            preserve_default=False,
        ),
    ]
