from django.urls import path

from ManageReview import views

app_name = 'ManageReview'
urlpatterns = [
    path('post/review/product/<int:product_id>', views.add_product_review, name='add-product-review'),
    path('post/review/store/<int:store_id>', views.add_store_review, name='add-store-review'),
    path('post/review/offer/<int:offer_id>', views.add_offer_review, name='add_offer_review'),
    path('EditReview/<int:review_id>', views.edit_review, name='edit_review'),
]
