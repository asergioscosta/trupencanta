from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import time

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    sobrenome = models.CharField(_('Sobrenome'), max_length=40)

    class Meta:
        verbose_name = _('Pessoa')
        verbose_name_plural = _('Pessoas') 

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    razao_social = models.CharField(_('Razão Social'), max_length = 30)
    cnpj = models.CharField(_('CNPJ'), max_length = 18, unique = True, help_text =_('Format: 00.000.000/0000-00'))
    email = models.EmailField(_('E-mail'), blank = True, max_length = 200, unique = True)

    class Meta:
        verbose_name = _('Instituição')
        verbose_name_plural = _('Instituições')

    def __str__(self):
        return self.razao_social

    def save(self, *args, **kwargs):
        # Remove non-numeric characters from CNPJ
        self.cnpj = ''.join(filter(str.isdigit, self.cnpj))

        # Add dots and dashes to the CNPJ
        self.cnpj = f'{self.cnpj[:2]}.{self.cnpj[2:5]}.{self.cnpj[5:8]}/{self.cnpj[8:12]}-{self.cnpj[12:18]}'

        super().save(*args, **kwargs)

class Professor(Pessoa):
    formacao = models.TextField(_('Formação'), max_length=255)

    instituicao = models.ForeignKey(Instituicao, null = False, on_delete = models.CASCADE)

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professores')

    def __str__(self):
        return self.formacao

class Endereco(models.Model):
    ufs = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    cep = models.CharField(_('CEP'), max_length=9)
    logradouro = models.CharField(_('Logradouro'), max_length=50)
    numero = models.CharField(_('Número'), max_length=10)
    complemento = models.CharField(_('Complemento'), blank=True, max_length=20)
    bairro = models.CharField(_('Bairro'), max_length=38)
    cidade = models.CharField(_('Cidade'), max_length=20)
    uf = models.CharField('UF', max_length=2, choices=ufs)
    
    instituicao = models.ForeignKey(Instituicao, null=False, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

    def __str__(self):
        return self.logradouro

    def save(self, *args, **kwargs):
        # Remove non-numeric characters from CEP
        self.cep = ''.join(filter(str.isdigit, self.cep))

        # Add dots and dashes to the  ao CEP
        self.cep = f'{self.cep[:5]}-{self.cep[5:]}'

        super().save(*args, **kwargs)

class Telefone(models.Model):
    telefone = (
    ('residencial', 'Telefone Residencial'),
    ('celular', 'Telefone Celular'),
    ('trabalho', 'Telefone Comercial')
    )

    numero = models.CharField(_('Número de Telefone'), max_length=20, blank=True, help_text=_('Formato: (xx) xxxxx-xxxx'))
    tipo = models.CharField('Tipo de Telefone', max_length=30, choices=telefone)

    instituicao = models.ForeignKey(Instituicao, null=False, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE)

    class Meta:
         verbose_name = _('Telefone')
         verbose_name_plural = _('Telefones')

    def __str__(self):
         return self.numero

    def save(self, *args, **kwargs):
        # Remove non-numeric characters from number
        self.numero = ''.join(filter(str.isdigit, self.numero))

        # Add dots and dashes to the Number
        formatted_numero = f'({self.numero[:2]}) {self.numero[2:7]}-{self.numero[7:]}'

        self.numero = formatted_numero

        super().save(*args, **kwargs)

class Documento (models.Model):
    nome = models.CharField(_('Nome'), max_length = 100)
    arquivo = models.FileField(upload_to = 'Documentos/')
    descricao = models.CharField(_('Descrição'), max_length = 100)

    instituicao = models.ForeignKey(Instituicao, null = False, on_delete = models.CASCADE)

    class Meta:
        verbose_name = _('Documento')
        verbose_name_plural = _('Documentos')

    def __str__(self):
        return self.nome

class Oficina(models.Model):
    dia_semana = (
        ('Segunda-Feira','Segunda-Feira'),
        ('Terça-Feira','Terça-Feira'),
        ('Quarta-Feira','Quarta-Feira'),
        ('Quinta-feira','Quinta-Feira'),
        ('Sexta-Feira','Sexta-Feira'),
        ('Sábado','Sábado'),
        ('Domingo','Domingo'),
    )

    nome = models.CharField(_('Nome'), max_length=100)
    imagem = models.ImageField(upload_to='Projetos/')
    resumo = models.CharField(_('Resumo'), max_length=155)
    area = models.TextField(_('Área da Oficina'), help_text='Insira a área da oficina, como Artes cênicas, canto')
    descricao = models.TextField(_('Descrição'), help_text='Insira uma descrição detalhada aqui.\nPule linhas conforme necessário.')
    dia_aulas = models.CharField(_('Dia das Aulas'), max_length=13, choices=dia_semana)
    horario = models.TimeField(choices=[(time(hour=h, minute=m), f"{h:02d}:{m:02d}") for h in range(8, 24) for m in range(0, 60, 30)])

    class Meta:
        verbose_name = _('Oficina')
        verbose_name_plural = _('Oficinas')

    def __str__(self):
        return self.nome

class Noticia(models.Model):
    titulo = models.CharField(_('Título'), max_length=255)
    imagem = models.ImageField(upload_to='Noticias/')
    resumo = models.CharField(_('Resumo'), max_length=155)
    area = models.TextField(_('Área da Oficina'), help_text='Insira a área da Notícia, como Artes cênicas, canto')
    data_publicacao = models.DateField(_('Data da Publicação'))
    data_evento = models.DateField(_('Data do Evento'))
    texto_noticia = models.TextField(_('Texto'))

    class Meta:
        verbose_name = _('Noticia')
        verbose_name_plural = _('Noticias')

    def __str__(self):
        return self.titulo
    
class Projeto(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    imagem = models.ImageField(upload_to='projetos/')
    descricao = models.CharField(_('Descrição'), max_length = 155)
    resumo = models.TextField(_('Resumo'))

    instituicao = models.ForeignKey(Instituicao, null = False, on_delete = models.CASCADE)
    oficina = models.ManyToManyField(Oficina)
    noticia = models.ManyToManyField(Noticia)

    class Meta:
        verbose_name = _('Projeto')
        verbose_name_plural = _('Projetos')

    def __str__(self):
        return self.nome