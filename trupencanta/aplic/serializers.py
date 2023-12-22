from rest_framework import serializers

from aplic.models import Projeto

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