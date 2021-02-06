from unittest import TestCase
from ManageProduct.models import Product


class TestProduct(TestCase):
    def test_save(self):
        product = Product.objects.create(
            name='testproduct',
            product_sections='Section 1',
            par_Code=123456789,
            discount=10,
            manufacturer='test 1',
            description='Description',
            number_Of_Copy=1000,
            price=13.99,
            image='http://placehold.it/900x400',
            type='Food'
        )

        self.assertTrue(isinstance(product, Product))

    def test_not_save(self):
        product = Product.objects.create()

        self.assertTrue(isinstance(product, Product))

    def testGetPriceAfterDiscount(self):
        product = Product.objects.create(
            name='testproduct',
            product_sections='Section 1',
            par_Code=123456789,
            discount=25,
            manufacturer='test 1',
            description='Description',
            number_Of_Copy=1000,
            price=100,
            image='http://placehold.it/900x400',
            type='Food'
        )

        self.assertEqual(75, product.grt_price_after_discount())
