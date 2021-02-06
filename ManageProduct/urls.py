from django.urls import path

from . import views
from .views import ProductAdmin ,ProductsCustomer

app_name = 'ManageProduct'
urlpatterns = [

    # path('ProductList/', ProductAdmin.view_all_products, name='view_all_products'),
    path('ProductCreate/', ProductAdmin.product_create, name='product_create'),
    path('ProductView/<int:pk>', ProductAdmin.product_view, name='product_view'),
    path('ProductUpdate/<int:pk>', ProductAdmin.update_product, name='update_product'),
    path('ProductDelete/<int:pk>', ProductAdmin.delete_product, name='delete_product'),
    # path('profilter/', views.profilter, name='profilter'),
    path('add_to_favorite/<int:id>', ProductsCustomer.add_to_favorite, name='add_to_favorite'),
    path('remove_to_favorite/<int:id>', ProductsCustomer.remove_to_favorite, name='remove_to_favorite'),

]
