from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.db.models import Q
from aplic.serializers import ProjetoSerializer
from rest_framework import viewsets, permissions
from .models import Projeto

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        query = self.request.GET.get("iptText")
        print(query)
        
        if (query is None):
            context['projeto'] = Projeto.objects.order_by('id').all()
            print('não tinha nada digitado no iptText')
        else:
            context['projeto'] = Projeto.objects.filter(Q(nome_curso__icontains=query))
            context['projeto'] = Projeto.objects.filter(Q(descricao__icontains=query))

        return context

class ProjetoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class SaibaMaisView(TemplateView):
    template_name = 'saiba-mais.html'