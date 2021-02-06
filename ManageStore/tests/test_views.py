from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from ManageStore.models import Store
from accounts.models import StoreAdminProfile


class TestStoreView(TestCase):
    def setUp(self) -> None:
        self.view_store_url = reverse('ManageStore:view_store', args=[1])
        self.edit_store_url = reverse('ManageStore:edit_store')
        self.create_store_url = reverse('ManageStore:create_store')
        self.client = Client()

    def testViewStore(self):
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
        response = self.client.get(self.view_store_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store.html')

    def testEditStore(self):
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
        response = self.client.get(reverse('ManageStore:edit_store'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_store.html')

    def testCreateStore(self):
        user = User.objects.create_user('storejohn', 'storelennon@thebeatles.com', 'johnpassword')
        user.save()

        store_profile = StoreAdminProfile.objects.create(
            user=user,
            slug='storejohn',
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
        )
        store_profile.save()

        self.client.login(username='storejohn', password='johnpassword')
        response = self.client.get(self.create_store_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Create_Store.html')
