from django.contrib.auth.models import User
from django.test import TestCase
from accounts.forms import SignupForm, StoreAdminEditForm, UserEditForm
from django.utils import timezone


class TestSignupForm(TestCase):
    def test_valid_form(self):
        form = SignupForm(
            data={
                'username': 'user102asd11',
                'password1': 'testpass1',
                'password2': 'testpass1',
                'first_name': 'user',
                'last_name': '1',
                'email': 'feras@gmail.com',
                'typee': 'Customer'
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = SignupForm(data={})

        self.assertFalse(form.is_valid())


class TestStoreAdminEditForm(TestCase):
    def test_valid_form(self):
        form = StoreAdminEditForm(
            data={
                'user': User.objects.create_user('asdfasdf', 'asdfasdf@gmail.com', 'Trespass'),
                'slug': 'asdfasdf',
                'image': 'http://placehold.it/900x400',
                'address': 'Amman',
                'join_at': timezone.now(),
                'country': 'JO',
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = StoreAdminEditForm(data={})
        self.assertFalse(form.is_valid())


class TestUserEditForm(TestCase):
    def test_valid_form(self):
        form = UserEditForm(
            data={
                'email': 'ferasasdakljsghasjl@gmail.com',
                'first_name': 'feras',
                'last_name': 'masoud',
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = UserEditForm(data={
            'email': 'xxx',
            'first_name': 'xxx',
            'last_name': 'xxx',
        })
        self.assertFalse(form.is_valid())


class TestCustomerForm(TestCase):
    def test_valid_form(self):
        form = UserEditForm(
            data={
                'address': 'Amman',
                'image': 'http://placehold.it/900x400',
                'country': 'JO',
            }
        )

        self.assertTrue(form.is_valid())
