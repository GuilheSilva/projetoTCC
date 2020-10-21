from django.urls import path
from .views import realEstate_list
from .views import realEstate_new
from .views import realEstate_update
from .views import realEstate_delete,voltar


urlpatterns = [
    path('list/', realEstate_list, name='realEstate_listing'),
    path('new/', realEstate_new, name='realEstate_add'),
    path('update/<int:id>', realEstate_update, name='realEstate_update'),
    path('list/delete/<int:id>', realEstate_delete, name='realEstate_delete'),
    path('voltar/', voltar, name='voltar'),

]