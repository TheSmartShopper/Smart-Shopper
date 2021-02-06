from unittest import TestCase

from ManageOffer.models import Offer


class TestOffer(TestCase):
    def test_save(self):
        offer = Offer.objects.create(
            name='offer1',
            expiratiDate='2021-05-01',
            state=True,
            number_OF_Copy=120,
            price=33.3,
            image='http://placehold.it/900x400',
            slug='offer1',
        )
        offer.save()

        self.assertTrue(isinstance(offer, Offer))
