from django.urls import path
from .views import home, my_logout, homePageSistema
#from .views import DashboardView
from .views import dashboardView



urlpatterns = [
    path('', home, name="home"),
    #path('sistema/', homePageSistema, name="sistema"),
    #path('sistema/', DashboardView.as_view(), name='sistema'),
    path('sistema/', dashboardView, name='sistema'),
    path('logout/', my_logout, name="logout"),

]