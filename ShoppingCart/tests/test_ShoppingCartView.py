from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from ManageProduct.models import Product
from accounts.CustomerProfilemodel import CustomerProfile


class Test(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user.save()

        self.user = user
        self.customer_profile = CustomerProfile.objects.create(
            user=self.user,
            slug='john',
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
        )
        self.customer_profile.save()

        product = Product.objects.create(name='product1')
        product.save()

        self.view_shopping_cart_url = reverse('ShoppingCart:view_shopping_cart')
        self.add_product_to_cart_url = reverse('ShoppingCart:add_product_to_cart', args=[product.id, 10])
        self.edit_product_quantity_cart_url = reverse('ShoppingCart:edit_product_quantity_cart', args=[product.id, 10])
        self.add_offer_to_cart_url = reverse('ShoppingCart:add_offer_to_cart', args=[product.id, 10])
        self.edit_offer_quantity_cart_url = reverse('ShoppingCart:edit_offer_quantity_cart', args=[product.id, 10])

    def test_view_shopping_cart(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.view_shopping_cart_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_shopping_cart.html')

    def test_add_product_to_cart(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.add_product_to_cart_url)
        self.assertEqual(response.status_code, 302)

    def test_edit_product_quantity_cart(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.edit_product_quantity_cart_url)
        self.assertEqual(response.status_code, 302)

    def test_add_offer_to_cart(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.add_offer_to_cart_url)
        self.assertEqual(response.status_code, 302)

    def test_edit_offer_quantity_cart(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.edit_offer_quantity_cart_url)
        self.assertEqual(response.status_code, 302)
