from unittest import TestCase
from django.urls import reverse, resolve
from ShoppingCart.ShoppingCartView import view_shopping_cart, add_product_to_cart, edit_product_quantity_cart, \
    add_offer_to_cart, edit_offer_quantity_cart


class Test(TestCase):
    def test_view_shopping_cart(self):
        url = reverse('ShoppingCart:view_shopping_cart')
        self.assertEqual(resolve(url).func, view_shopping_cart)

    def test_add_product_to_cart(self):
        url = reverse('ShoppingCart:add_product_to_cart', args=[1, 1])
        self.assertEqual(resolve(url).func, add_product_to_cart)

    def test_edit_product_quantity_cart(self):
        url = reverse('ShoppingCart:edit_product_quantity_cart', args=[1, 1])
        self.assertEqual(resolve(url).func, edit_product_quantity_cart)

    # def test_add_offer_to_cart(self):
    #     url = reverse('ShoppingCart:add_offer_to_cart', args=[0, 0])
    #     self.assertEqual(resolve(url).func, add_offer_to_cart)
    #
    # def test_edit_offer_quantity_cart(self):
    #     url = reverse('ShoppingCart:edit_offer_quantity_cart', args=[0, 0])
    #     self.assertEqual(resolve(url).func, edit_offer_quantity_cart)
