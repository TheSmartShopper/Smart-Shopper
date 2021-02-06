from django.test import Client, TestCase, RequestFactory
from django.urls import reverse
from ManageStore.models import Store
from django.contrib.auth.models import User
from ManageProduct.views import *


class TestProductAdmin(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.factory = RequestFactory()
        self.product_create_url = reverse('ManageProduct:product_create')
        self.product_view_url = reverse('ManageProduct:product_view', args=[1])
        self.product = Product.objects.create(name='Product1')
        self.product.save()

    def testProductCreateGet(self):
        user = User.objects.create_user('storejohn', 'storelennon@thebeatles.com', 'johnpassword')
        user.save()

        store = Store.objects.create(name='store1')
        store.save()

        store_profile = StoreAdminProfile.objects.create(
            user=user,
            slug='storejohn',
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
            store=store,
        )
        store_profile.save()

        self.client.login(username='storejohn', password='johnpassword')
        response = self.client.get(self.product_create_url, follow=True)
        self.assertEquals(response.status_code, 200)

    def testProductCreatePost(self):
        user = User.objects.create_user('storejohn', 'storelennon@thebeatles.com', 'johnpassword')
        user.save()

        store = Store.objects.create(name='store1')
        store.save()

        store_profile = StoreAdminProfile.objects.create(
            user=user,
            slug='storejohn',
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
            store=store,
        )
        store_profile.save()

        self.client.login(username='storejohn', password='johnpassword')
        response = self.client.post(self.product_create_url, follow=True)
        self.assertEquals(response.status_code, 200)

    def testProductView(self):
        response = self.client.get(self.product_view_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_home.html')

    def testUpdateProduct(self):
        user = User.objects.create_user('storejohn', 'storelennon@thebeatles.com', 'johnpassword')
        user.save()

        store = Store.objects.create(name='store1')
        store.save()

        store_profile = StoreAdminProfile.objects.create(
            user=user,
            slug='storejohn',
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
            store=store,
        )

        product = store_profile.store.products.create(
            name='product1'
        )

        product.save()
        store_profile.save()

        product_update_url = reverse(
            'ManageProduct:update_product',
            args=[product.id]
        )

        self.client.login(username='storejohn', password='johnpassword')
        response = self.client.get(product_update_url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_add_form.html')
