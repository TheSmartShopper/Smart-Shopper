from unittest import TestCase
from django.urls import reverse, resolve
from ManageReview.views import edit_review, add_store_review, add_product_review, add_offer_review


class TestUrls(TestCase):
    def testEditReview(self):
        url = reverse('ManageReview:edit_review', args=[1])
        self.assertEqual(resolve(url).func, edit_review)

    def testAddProductReview(self):
        url = reverse('ManageReview:add-product-review', args=[1])
        self.assertEqual(resolve(url).func, add_product_review)

    def testAddStoreReview(self):
        url = reverse('ManageReview:add-store-review', args=[1])
        self.assertEqual(resolve(url).func, add_store_review)

    def testAddOfferReview(self):
        url = reverse('ManageReview:add_offer_review', args=[1])
        self.assertEqual(resolve(url).func, add_offer_review)
