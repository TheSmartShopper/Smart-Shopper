from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from accounts.CustomerProfilemodel import CustomerProfile
from accounts.forms import SignupForm
from accounts.models import StoreAdminProfile
from ManageStore.models import Store


class TestSignUpView(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.signup_url = reverse('accounts:signup')

    def test_form_valid(self):
        form_data = {
            'username': 'ferasmasoud',
            'password1': 'testpass1',
            'password2': 'testpass1',
            'first_name': 'feras',
            'last_name': 'masoud',
            'email': 'feras.masoud1998@gmail.com',
            'typee': 'Customer',
        }

        form = SignupForm(form_data)
        self.assertTrue(form.is_valid())

    def test_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')


class TestCustomerViews(TestCase):
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

        self.customer_profile_url = reverse('accounts:CustomerProfileView')
        self.customer_edit_profile_url = reverse('accounts:Customer_Edit_Profile_View')

    def test_customer_profile_view(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.customer_profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CustomerProfile.html')

    def test_customer_edit_profile_view(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(self.customer_edit_profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, '404.html')


class TestStoreAdminViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        user = User.objects.create_user('storejohn', 'storelennon@thebeatles.com', 'johnpassword')
        user.save()

        store = Store.objects.create(name='store',)
        store.save()

        self.store = store
        self.user = user
        self.store_profile = StoreAdminProfile.objects.create(
            user=self.user,
            slug='storejohn',
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
            store=self.store,
        )
        self.store_profile.save()

        self.store_admin_profile_view_url = reverse('accounts:StoreAdminProfileView')
        self.store_admin_edit_profile_view_url = reverse('accounts:StoreAdminEditProfileView')

    def test_store_admin_profile_view(self):
        self.client.login(username='storejohn', password='johnpassword')
        response = self.client.get(self.store_admin_profile_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'StoreAdminProfile.html')

    def test_store_admin_edit_profile_view_GET(self):
        self.client.login(username='storejohn', password='johnpassword')
        response = self.client.get(self.store_admin_edit_profile_view_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'StoreAdminEditInfo.html')

    def test_store_admin_edit_profile_view_POST(self):
        self.client.login(username='storejohn', password='johnpassword')
        response = self.client.post(self.store_admin_edit_profile_view_url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'StoreAdminProfile.html')
