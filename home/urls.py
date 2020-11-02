from django.urls import path
from .views import home, my_logout, homePageSistema
# from .views import DashboardView
from .views import dashboardView, configLogin

urlpatterns = [
    path('', home, name="home"),
    # path('sistema/', homePageSistema, name="sistema"),
    # path('sistema/', DashboardView.as_view(), name='sistema'),
    path('sistema/', dashboardView, name='sistema'),
    path('loginConf/', configLogin, name='loginConf'),
    #path('conf/', configLogin, name='conf'),
    # path('charts/', charts, name='charts'),
    path('logout/', my_logout, name="logout"),

]
