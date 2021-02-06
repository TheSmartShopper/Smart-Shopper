from unittest import TestCase
from accounts.models import StoreAdminProfile
from accounts.CustomerProfilemodel import CustomerProfile
from ManageStore.models import Store
from django.contrib.auth.models import User


class TestStoreAdminProfile(TestCase):
    def test_save(self):
        user = User.objects.create_user('johnasdsdstestuser', 'lasdennonuser@thebeatles.com', 'johnpassword')
        user.save()
        store = Store.objects.create(name='store')
        store.save()

        storeadmin = StoreAdminProfile.objects.create(
            user=user,
            store=store,
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
        )
        storeadmin.save()

        self.assertTrue(isinstance(storeadmin, StoreAdminProfile))


class TestCustomerProfile(TestCase):
    def test_save(self):
        user = User.objects.create_user('ferasusertest1', 'feras@thebeatles.com', 'feraspass')
        user.save()

        customer_profile = CustomerProfile.objects.create(
            user=user,
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
        )
        customer_profile.save()

        self.assertTrue(isinstance(customer_profile, CustomerProfile))
