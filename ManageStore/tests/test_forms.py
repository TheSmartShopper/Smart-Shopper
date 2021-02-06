from unittest import TestCase
from ManageStore.forms import CreateStoreForm


class TestCreateStoreForm(TestCase):
    def test_valid_form(self):
        form = CreateStoreForm(
            data={
                'name': 'Sameh Mall',
                'image': 'http://placehold.it/900x400',
                'phonesNumber': '+962796934976',
                'start_hours': '8:00:00',
                'close_hours': '22:00:00',
                'description': 'asfadfgadf',
                'state': True,
                'type': 'BigMarket',
                'url': 'http://placehold.it/900x400',
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = CreateStoreForm(data={})

        self.assertFalse(form.is_valid())


class TestEditStoreForm(TestCase):
    def test_valid_form(self):
        form = CreateStoreForm(
            data={
                'name': 'Sameh Mall',
                'image': 'http://placehold.it/900x400',
                'phonesNumber': '+962796934976',
                'start_hours': '8:00:00',
                'close_hours': '22:00:00',
                'description': 'asfadfgadf',
                'state': True,
                'type': 'BigMarket',
                'url': 'http://placehold.it/900x400',
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = CreateStoreForm(data={})
        self.assertFalse(form.is_valid())
