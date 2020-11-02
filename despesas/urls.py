
from django.urls import path
from .views import despesas_new,despesas_list, despesas_edit, deletar_despesa


urlpatterns = [
    path('nova/', despesas_new, name='despesas'),
    path('editar/<int:id>', despesas_edit, name='despesas_edit'),
    path('list/', despesas_list, name='despesas_list'),
    path('delete/<int:id>', deletar_despesa, name='delete')
]