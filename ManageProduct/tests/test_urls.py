from unittest import TestCase
from django.urls import reverse, resolve
from ManageProduct.views import ProductAdmin, ProductsCustomer


class TestUrls(TestCase):
    def testProductCreate(self):
        url = reverse('ManageProduct:product_create')
        self.assertEquals(
            resolve(url).func,
            ProductAdmin.product_create
        )

    def testProductView(self):
        url = reverse(
            'ManageProduct:product_view',
            args=[1],
        )
        self.assertEquals(
            resolve(url).func,
            ProductAdmin.product_view
        )

    def testProductUpdate(self):
        url = reverse(
            'ManageProduct:update_product',
            args=[1],
        )
        self.assertEquals(
            resolve(url).func,
            ProductAdmin.update_product
        )

    def testProductDelete(self):
        url = reverse(
            'ManageProduct:delete_product',
            args=[1],
        )
        self.assertEquals(
            resolve(url).func,
            ProductAdmin.delete_product
        )

    def testAddToFavorite(self):
        url = reverse(
            'ManageProduct:add_to_favorite',
            args=[1],
        )
        self.assertEquals(
            resolve(url).func,
            ProductsCustomer.add_to_favorite
        )

    def testDeleteFromFavorite(self):
        url = reverse(
            'ManageProduct:remove_to_favorite',
            args=[1],
        )
        self.assertEquals(
            resolve(url).func,
            ProductsCustomer.remove_to_favorite
        )
