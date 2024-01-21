from django.urls import path
from .views import ContatoView, continuealer, EstacaoTrupeSolidariaView, IndexView, NoticiaView, OficinaView, ProjetoEstacaoCulturalView, ProjetoEstacaoCircuitoCulturalView, saibamais, SobreNosView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('continuealer/<int:noticia_id>/', continuealer, name='continue-a-ler'),
    path('projeto-estacao-cultural', ProjetoEstacaoCulturalView.as_view(), name='projeto-estacao-cultural'),
    path('estacao-trupe-solidaria', EstacaoTrupeSolidariaView.as_view(), name='estacao-trupe-solidaria'),
    path('projeto-estacao-circuito-cultural', ProjetoEstacaoCircuitoCulturalView.as_view(), name='projeto-estacao-circuito-cultural'),
    path('index/', IndexView.as_view(), name='projeto'),
    path('noticias/', NoticiaView.as_view(), name ='noticia' ),
    path('oficina/', OficinaView.as_view(), name ='oficina' ),
    path('saibamais/<int:oficina_id>/', saibamais, name='saibamais'),
    path('sobre-nos/', SobreNosView.as_view(), name='sobre-nos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)