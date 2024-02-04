from django.views.generic import TemplateView
from django.db.models import Q
from aplic.serializers import ProjetoSerializer, OficinaSerializer, NoticiaSerializer, ProfessorSerializer
from rest_framework import viewsets, permissions
from .models import Projeto, Oficina, Noticia, Professor
from .forms import ContatoForm
from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

# Create your views here.

class ContatoView(TemplateView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'), extra_tags='success')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Falha ao enviar e-mail'), extra_tags='danger')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)

def continuealer(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)
    return render(request, 'continue-a-ler.html', {'noticia': noticia})

class EstacaoTrupeSolidariaView(TemplateView):
    template_name = 'estacao-trupe-solidaria.html'

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        query = self.request.GET.get("iptText")
        print(query)
        
        if (query is None):
            context['projeto'] = Projeto.objects.order_by('id').all()
        else:
            context['projeto'] = Projeto.objects.filter(Q(nome_curso__icontains=query))
            context['projeto'] = Projeto.objects.filter(Q(descricao__icontains=query))

        return context

class NoticiaView(TemplateView):
    template_name = 'noticias.html'

    def get_context_data(self, **kwargs):
        context = super(NoticiaView, self).get_context_data(**kwargs)
        
        query = self.request.GET.get("iptText")
        print(query)
        
        if (query is None):
            context['noticia'] = Noticia.objects.order_by('id').all()
        else:
            context['noticia'] = Noticia.objects.filter(Q(nome__icontains=query))
            context['noticia'] = Noticia.objects.filter(Q(descricao__icontains=query))
    
        context['latest_posts'] = Noticia.objects.order_by('-data_publicacao')[:3]

        return context
    
class NoticiaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class OficinaView(TemplateView):
    template_name = 'oficina.html'

    def get_context_data(self, **kwargs):
        context = super(OficinaView, self).get_context_data(**kwargs)
        
        query = self.request.GET.get("iptText")
        print(query)
        
        if (query is None):
            context['oficina'] = Oficina.objects.order_by('id').all()
        else:
            context['oficina'] = Oficina.objects.filter(Q(nome__icontains=query))
            context['oficina'] = Oficina.objects.filter(Q(descricao__icontains=query))

        return context

class OficinaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Oficina.objects.all()
    serializer_class = OficinaSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    
class ProjetoEstacaoCulturalView(TemplateView):
    template_name = 'projeto-estacao-cultural.html'

class ProjetoEstacaoCircuitoCulturalView(TemplateView):
    template_name = 'projeto-estacao-circuito-cultural.html'

def saibamais(request, oficina_id):
    oficina = Oficina.objects.get(pk=oficina_id)
    return render(request, 'saibamais.html', {'oficina': oficina})

class SobreNosView(TemplateView):
    template_name = 'sobre-nos.html'

    def get_context_data(self, **kwargs):
        context = super(SobreNosView, self).get_context_data(**kwargs)
        
        query = self.request.GET.get("iptText")
        print(query)
        
        if (query is None):
            context['professor'] = Professor.objects.order_by('id').all()
        else:
            context['professor'] = Professor.objects.filter(Q(nome__icontains=query))
            context['professor'] = Professor.objects.filter(Q(curso__icontains=query))

        return context

class SobreNosViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, )

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer