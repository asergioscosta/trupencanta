from django.urls import path
from .views import IndexView, SaibaMaisView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('saiba-mais/', SaibaMaisView.as_view(), name='saiba-mais'),
    path('index/', IndexView.as_view(), name='projeto'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)