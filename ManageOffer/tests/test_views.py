from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ManageOffer.models import Offer
from ManageStore.models import Store
from accounts.models import StoreAdminProfile


class Test(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        user = User.objects.create_user('storejohntest', 'storelennon@thebeatles.com', 'johnpassword')
        user.save()

        store = Store.objects.create(name='store')
        store.save()

        self.user = user
        self.store = store

        self.store_profile = StoreAdminProfile.objects.create(
            user=self.user,
            slug='storejohntest',
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
            store=self.store,
        )
        self.store_profile.save()

        self.create_offer_url = reverse('ManageOffer:create_offer')
        self.edit_offer_url = reverse('ManageOffer:edit_offer', args=[1])
        self.delete_offer_url = reverse('ManageOffer:delete_offer', args=[1])

    def testCreateOffer(self):
        self.client.login(username='storejohntest', password='johnpassword')

        response = self.client.get(self.create_offer_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_offer.html')

    def testEditOffer(self):
        self.client.login(username='storejohntest', password='johnpassword')

        offer = Offer.objects.create(
            name='offer1',
            expiratiDate='2021-05-01',
            state=True,
            number_OF_Copy=120,
            price=33.3,
            image='http://placehold.it/900x400',
            slug='offer1',
        )

        product = offer.products.create(name='product1')
        product.save()
        offer.save()

        response = self.client.get(self.edit_offer_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Edit_Offer.html')
