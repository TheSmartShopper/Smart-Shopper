from django.urls import path
from ManageOffer import views

app_name = 'ManageOffer'
urlpatterns = [
    path('view_all_offers/', views.view_all_offers, name='view_all_offers'),
    # path('view_store_offers/', views.view_store_offers, name='view_store_offers'),
    path('view_offer/<offer_id>', views.view_offer, name='view_offer'),
    path('create_offer/', views.create_offer, name='create_offer'),
    path('edit_offer/<offer_id>', views.edit_offer, name='edit_offer'),
    path('delete_offer/<offer_id>', views.delete_offer, name='delete_offer'),

]
