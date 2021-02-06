from unittest import TestCase
from ManageOffer.forms import OfferForm


class TestOfferForm(TestCase):
    def test_valid_form(self):
        form = OfferForm(
            data={
                'name': 'offer1',
                'expiratiDate': '2021-05-01',
                'state': 'True',
                'number_OF_Copy': 120,
                'price': 33.3,
                'image': 'http://placehold.it/900x400',
                'slug': 'offer1',
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = OfferForm(data={})

        self.assertFalse(form.is_valid())
