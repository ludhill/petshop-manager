# management/urls.py
from django.urls import path
from .views import (
    TipoAnimalListView,
    TipoAnimalCreateView,
    RacaListView,
    RacaCreateView,
    get_racas_by_tipo,
    AnimalCreateView,
    #error_500_test_view # Importe a view TESTANDO 500
)

urlpatterns = [
    path('tipos/', TipoAnimalListView.as_view(), name='tipoanimal_list'),
    path('tipos/novo/', TipoAnimalCreateView.as_view(), name='tipoanimal_create'),
    path('racas/', RacaListView.as_view(), name='raca_list'),
    path('racas/nova/', RacaCreateView.as_view(), name='raca_create'),
    path('api/get-racas/', get_racas_by_tipo, name='api_get_racas'),
    path('animal/novo/', AnimalCreateView.as_view(), name='animal_create'),
    # A linha do admin foi REMOVIDA daqui.
    #path('teste-erro-500/', error_500_test_view, name='teste_erro_500'),
] 