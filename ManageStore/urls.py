from django.urls import path

from ManageStore import views

app_name = 'ManageStore'
urlpatterns = [

    path('Store/Detail/<int:store_id>', views.view_store, name='view_store'),
    path('Store/Detail/<int:store_id>/<str:section>', views.products_in_section, name='view_store_section'),
    path('Store/Create', views.create_store, name='create_store'),
    path('Edit/Store/Detail', views.edit_store, name='edit_store'),
    path('add/ad_img/', views.add_ADs, name='add_ADs'),
    path('delete/ad_img/<int:ad_id>', views.delete_ADs, name='delete_ADs'),


]
