from django.contrib import admin
from aplic.models import Documento, Endereco, Instituicao, Noticia, Oficina, Professor, Projeto, Telefone

# Register your models here.

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'arquivo', 'descricao') 

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf')

@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'email') 

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagem', 'resumo', 'area', 'data_publicacao', 'data_evento', 'texto_noticia') 

@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'resumo', 'area', 'horario', 'dia_aulas')
    
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('formacao', 'cargo', 'imagem') 

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'resumo')

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo')