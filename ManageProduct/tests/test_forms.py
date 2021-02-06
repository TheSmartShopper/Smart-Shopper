from unittest import TestCase
from ManageProduct.forms import ProductForm


class TestProductForm(TestCase):
    def test_valid_form(self):
        form = ProductForm(
            data={
                'name': 'user102asd11',
                'price': 33.6,
                'type': 'Beverages',
                'number_Of_Copy': 123,
                'par_Code': 12345678,
                'description': 'asfadgdfasf',
                'manufacturer': 'Manufacturer 1',
                'image': 'http://placehold.it/900x400',
                'discount': 0.3,
                'sections': 'Food'
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())
