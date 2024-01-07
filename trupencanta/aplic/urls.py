from django.urls import path
from .views import ContatoView, continuealer, IndexView, NoticiaView, OficinaView, ProjetoEstacaoCulturalView, saibamais 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('continuealer/<int:noticia_id>/', continuealer, name='continue-a-ler'),
    path('estacao-cultural', ProjetoEstacaoCulturalView.as_view(), name='projeto-estacao-cultural'),
    path('index/', IndexView.as_view(), name='projeto'),
    path('noticias/', NoticiaView.as_view(), name ='noticia' ),
    path('oficina/', OficinaView.as_view(), name ='oficina' ),
    path('saibamais/<int:oficina_id>/', saibamais, name='saibamais'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)