from django.urls import path
from .views import IndexView, saibamais, OficinaView, ContatoView, ProjetoEstacaoCulturalView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('saibamais/<int:oficina_id>/', saibamais, name='saibamais'),
    path('index/', IndexView.as_view(), name='projeto'),
    path('oficina/', OficinaView.as_view(), name ='oficina' ),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('estacao-cultural', ProjetoEstacaoCulturalView.as_view(), name='projeto-estacao-cultural'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)