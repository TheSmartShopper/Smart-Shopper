from unittest import TestCase

from ManageOffer.models import Offer
from ManageProduct.models import Product
from ShoppingCart.models import CartItem, CartOffer, ShoppingCart


class TestCartItem(TestCase):
    def test_save(self):
        cartitem = CartItem.objects.create(
            added_at='08:00:00',
            quantity=100,
            product=Product.objects.create(name='product1')
        )

        self.assertTrue(isinstance(cartitem, CartItem))


class TestCartOffer(TestCase):
    def test_save(self):
        cartoffer = CartOffer.objects.create(
            added_at='08:00:00',
            quantity=100,
            Offer=Offer.objects.create(name='offer-abc')
        )

        self.assertTrue(isinstance(cartoffer, CartOffer))


class TestShoppingCart(TestCase):
    def test_save(self):
        shopping_cart = ShoppingCart.objects.create(
            is_finished_adding=True,
        )

        self.assertTrue(isinstance(shopping_cart, ShoppingCart))

    def test_get_cart_total(self):
        shopping_cart = ShoppingCart.objects.create(
            is_finished_adding=True,
        )

        self.assertEqual(0, shopping_cart.get_cart_total())

    def test_get_product_ids(self):
        shopping_cart = ShoppingCart.objects.create(
            is_finished_adding=True,
        )

        self.assertEqual([], shopping_cart.get_product_ids())

    def test_get_offer_ids(self):
        shopping_cart = ShoppingCart.objects.create(
            is_finished_adding=True,
        )

        self.assertEqual([], shopping_cart.get_offer_ids())
