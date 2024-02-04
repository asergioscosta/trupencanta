from rest_framework import serializers

from aplic.models import Projeto, Oficina, Noticia, Professor

class NoticiaSerializer(serializers.ModelSerializer):
    disciplinas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='disciplina-detail')

    class Meta:
        model = Noticia
        fields = (
            'titulo',
            'imagem',
            'resumo',
            'area',
            'data_publicacao',
            'data_evento',
            'dia_aulas',
            'texto_noticia',
        )

class OficinaSerializer(serializers.ModelSerializer):
    disciplinas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='disciplina-detail')

    class Meta:
        model = Oficina
        fields = (
            'nome',
            'imagem',
            'descricao',
            'resumo',
            'dia_aulas',
            'horario',
        )

class ProjetoSerializer(serializers.ModelSerializer):
    disciplinas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='disciplina-detail')

    class Meta:
        model = Projeto
        fields = (
            'nome',
            'imagem',
            'descricao',
            'resumo',
        )

class ProfessorSerializer(serializers.ModelSerializer):
    professor = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='professor-detail')

    class Meta:
        model = Professor
        fields = (
            'imagem',
            'formacao',
            'cargo',
        )

