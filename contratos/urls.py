from django.urls import path
from .views import (create_contrato,
                    lista_contratos,
                    contratoDetail,
                    doc_contrato,
                    doc_list,
                    doc_delete,
                    photo_create,
                    geracontrato,
                    encerra_contrato)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
      path('new/', create_contrato, name='contrato_add'),
      path('lista/', lista_contratos, name='listagem_contratos'),
      path('detalhe_contrato/<int:id>', contratoDetail, name='detalhe_contrato'),
      path('detalhe_contrato/<int:id>/documento', doc_contrato, name='documento'),
      #path('documentoview/<int:id>', doc_list, name='documentoview'),
      path('documentdel/<int:id>', doc_delete, name='documentdel'),
      path('detalhe_contrato/<int:id>/photo', photo_create, name='photo'),
      path('printcontrato/<int:id>', geracontrato, name='printcontrato'),
      path('encerramento/<int:id>', encerra_contrato, name='encerramento'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)