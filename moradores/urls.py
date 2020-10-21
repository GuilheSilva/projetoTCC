from django.urls import path
from .views import residents_list
from .views import residents_delete, residents_update,residents_new,voltarMorador

urlpatterns = [
    path('list/', residents_list, name='lista_moradores'),
    path('update/<int:id>/', residents_update, name="residents_update"),
    path('list/delete/<int:id>/', residents_delete, name="residents_delete"),
    path('new/', residents_new, name="residentes_new"),
    path('voltarMorador/', voltarMorador, name='voltarMorador'),
]