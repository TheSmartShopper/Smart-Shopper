from django.urls import path

from Dashboard import views

app_name = 'Dashboard'
urlpatterns = [
    path('', views.Home, name='Home'),
    path('section/<str:sec>', views.section, name='section'),
    path('filter', views.productsfilter, name='filter'),
    path('search', views.search, name='search'),
    path('Maptest', views.Maptest,name='Maptest')
]
