# Generated by Django 4.2.8 on 2023-12-17 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=30, verbose_name='Razão Social')),
                ('cnpj', models.CharField(help_text='Format: 00.000.000/0000-00', max_length=18, unique=True, verbose_name='CNPJ')),
                ('email', models.EmailField(blank=True, max_length=200, unique=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Instituição',
                'verbose_name_plural': 'Instituições',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=40, verbose_name='Sobrenome')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.pessoa')),
                ('formacao', models.TextField(max_length=255, verbose_name='Formação')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
            bases=('aplic.pessoa',),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(blank=True, help_text='Formato: (xx) xxxxx-xxxx', max_length=20, verbose_name='Número de Telefone')),
                ('tipo', models.CharField(choices=[('residencial', 'Telefone Residencial'), ('celular', 'Telefone Celular'), ('trabalho', 'Telefone Comercial')], max_length=30, verbose_name='Tipo de Telefone')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.instituicao')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.pessoa')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=50, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=20, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=38, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=20, verbose_name='Cidade')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.instituicao')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.pessoa')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('arquivo', models.FileField(upload_to='Documentos/')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.instituicao')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]