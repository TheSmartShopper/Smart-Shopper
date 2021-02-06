from django.urls import path

from ShoppingCart import ShoppingCartView as view

app_name = "ShoppingCart"

urlpatterns = [

    path('viwe', view.view_shopping_cart, name='view_shopping_cart'),
    path('add/product/<int:product_id>/quantity/<int:quantity>', view.add_product_to_cart, name='add_product_to_cart'),
    path('edit/product/<int:product_id>/quantity/<int:quantity>', view.edit_product_quantity_cart,
         name='edit_product_quantity_cart'),
    path('add/product/<int:product_id>/quantity/<int:quantity>', view.add_offer_to_cart, name='add_offer_to_cart'),
    path('edit/product/<int:CartOffer_id>/quantity/<int:quantity>', view.edit_offer_quantity_cart,
         name='edit_offer_quantity_cart'),

    path('test/', view.mainUseCase, name='mainUseCase')

]
