from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.db.models import Q
from aplic.serializers import ProjetoSerializer, OficinaSerializer
from rest_framework import viewsets, permissions
from .models import Projeto, Oficina
from django.shortcuts import render

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

class OficinaView(TemplateView):
    template_name = 'oficina.html'

    def get_context_data(self, **kwargs):
        context = super(OficinaView, self).get_context_data(**kwargs)
        
        query = self.request.GET.get("iptText")
        print(query)
        
        if (query is None):
            context['oficina'] = Oficina.objects.order_by('id').all()
            print('não tinha nada digitado no iptText')
        else:
            context['oficina'] = Oficina.objects.filter(Q(nome__icontains=query))
            context['oficina'] = Oficina.objects.filter(Q(descricao__icontains=query))

        return context

class OficinaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Oficina.objects.all()
    serializer_class = OficinaSerializer

class BaleView(TemplateView):
    template_name = 'bale.html'

def saibamais(request, oficina_id):
    oficina = Oficina.objects.get(pk=oficina_id)
    return render(request, 'saibamais.html', {'oficina': oficina})
