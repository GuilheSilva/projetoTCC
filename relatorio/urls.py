from django.urls import path
from .views import relatorio_contratos_pdf, despesas_relatorio, relatorio_geral, relatorio_contratos, relatorio_despesas, print_relatorio


urlpatterns = [
    path('relatorio_contratos_pdf/', relatorio_contratos_pdf, name='relatorio_contratos_pdf'),
    #path('relatorio_despesas/', despesas_relatorio, name='despesas_relatorio'),
    path('relatorio_geral/', relatorio_geral, name='relatorio_geral'),
    path('relatorio_contratos/', relatorio_contratos, name='relatorio_contratos'),
    path('relatorio_despesas/', relatorio_despesas, name='relatorio_despesas'),
    path('print_relatorio/', print_relatorio, name='print_relatorio'),

    #path('gerar_relatorio_pdf/', gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
    #path('relatorio_contratos_html', Pdf.as_view(), name='relatorio_contratos_html'),
    #path('relatorio_contratos_html_debug', PdfDebug.as_view(), name='relatorio_contratos_html_debug'),
]