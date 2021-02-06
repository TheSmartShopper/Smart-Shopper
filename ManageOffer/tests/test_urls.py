from unittest import TestCase
from django.urls import reverse, resolve
from ManageOffer.views import view_offer, create_offer, edit_offer, delete_offer


class TestUrls(TestCase):

    def testViewOffer(self):
        url = reverse('ManageOffer:view_offer', args=[1])
        self.assertEqual(resolve(url).func, view_offer)

    def testCreateOffer(self):
        url = reverse('ManageOffer:create_offer')
        self.assertEqual(resolve(url).func, create_offer)

    def testEditOffer(self):
        url = reverse('ManageOffer:edit_offer', args=[1])
        self.assertEqual(resolve(url).func, edit_offer)

    def testDeleteOffer(self):
        url = reverse('ManageOffer:delete_offer', args=[1])
        self.assertEqual(resolve(url).func, delete_offer)
