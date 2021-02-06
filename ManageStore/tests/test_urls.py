from unittest import TestCase
from django.urls import reverse, resolve
from ManageStore.views import view_store, edit_store, create_store


class Test(TestCase):
    def test_view_store(self):
        url = reverse('ManageStore:view_store', args=[1])
        self.assertEqual(resolve(url).func, view_store)

    def test_edit_store(self):
        url = reverse('ManageStore:edit_store')
        self.assertEqual(resolve(url).func, edit_store)

    def test_create_store(self):
        url = reverse('ManageStore:create_store')
        self.assertEqual(resolve(url).func, create_store)
