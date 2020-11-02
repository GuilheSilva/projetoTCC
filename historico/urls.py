from django.urls import path
from .views import historicoview, quebra_contrato, historicoDetail,geracontratoHist

urlpatterns = [
    path('lista/', historicoview, name='historico'),
    path('printHist/<int:id>', geracontratoHist, name='printHist'),
    path('print_quebra/<int:id>', quebra_contrato, name='print_quebra'),
    path('historicoDetail/<int:id>', historicoDetail, name='historicoDetail'),
]
