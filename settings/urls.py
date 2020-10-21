from django.urls import path
from .views import settings,import_imoveis,import_moradores,dados_proprietario,update_proprietario




urlpatterns = [
    path('settings/', settings, name="settings"),
    path('dados/', dados_proprietario, name='dados'),
    path('importImoveis/', import_imoveis, name='import'),
    path('importMoradores/', import_moradores, name='import'),
    path('update/', update_proprietario, name='update'),

]