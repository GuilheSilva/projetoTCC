"""condado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from imoveis import urls as imoveis_urls
from moradores import urls as morador_urls
from django.contrib.auth import views as auth_views
from relatorio import urls as relatorio_urls
from django.conf import settings
from home import urls as home_urls
from contratos import urls as contratos_urls
from historico import urls as historico_urls
from relatorio import urls as relatorio_urls
from proprietario import urls as proprietarios_urls
from settings import urls as settings_urls
from despesas import urls as despesas_urls

urlpatterns = [
                  path('', include(home_urls)),
                  # path('sistema', include(home_urls)),
                  path('admin/clearcache/', include('clearcache.urls')),
                  path('admin/', admin.site.urls),
                  #path('admin/clearcache/', include('clearcache.urls')),
                  # path('config/', include(home_urls)),
                  # path('login/',auth_views.LoginView.as_view(), name='login'),
                  # path('login/', views.login_user, name='login'),
                  # path('login/autenticacao_user', views.autenticacao_user),
                  path('relatorio/', include(relatorio_urls)),
                  path('morador/', include(morador_urls)),
                  path('imoveis/', include(imoveis_urls)),
                  path('contrato/', include(contratos_urls)),
                  path('historico/', include(historico_urls)),
                  # path('accounts/', include('allauth.urls')),
                  path('accounts/', include('allauth.urls')),
                  path('', include('django.contrib.auth.urls')),
                  path('proprietario/', include(proprietarios_urls)),
                  path('settings/', include(settings_urls)),
                  path('despesas/', include(despesas_urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
