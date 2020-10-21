from django.urls import path
from .views import historicoview


urlpatterns = [
     path('lista/', historicoview, name='historico'),
]