from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from ManageReview.views import add_product_review, add_store_review

from ManageProduct.models import Product
from ManageStore.models import Store
from accounts.CustomerProfilemodel import CustomerProfile
from ManageReview.models import Review


class Test(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.factory = RequestFactory()

        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.customer_profile = CustomerProfile.objects.create(
            user=self.user,
            slug='john',
            image='http://placehold.it/900x400',
            address='Amman',
            country='Jordan',
        )

        self.edit_review_url = reverse('ManageReview:edit_review', args=[1])
        self.add_product_review_url = reverse('ManageReview:add-product-review', args=[1])
        self.add_store_review_url = reverse('ManageReview:add-store-review', args=[1])

    def test_add_product_review(self):
        product = Product.objects.create(name='product1')
        product.save()

        request = self.factory.get(reverse('ManageReview:add-product-review', args=[product.id]))
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = add_product_review(request, product_id=product.id)
        self.assertEqual(response.status_code, 302)

    def test_add_store_review(self):
        store = Store.objects.create(name='store1')
        store.save()

        request = self.factory.get(reverse('ManageReview:add-store-review', args=[store.id]), follow=True)
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = add_store_review(request, store_id=store.id)
        self.assertEqual(response.status_code, 302)

    def test_add_offer_review(self):
        store = Store.objects.create(name='store1')
        store.save()

        request = self.factory.get(reverse('ManageReview:add_offer_review', args=[store.id]), follow=True)
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = add_store_review(request, store_id=store.id)
        self.assertEqual(response.status_code, 302)

    def test_edit_review(self):
        review = Review.objects.create(
            rating=5,
            text='test'
        )
        review.save()

        request = self.factory.get(reverse('ManageReview:edit_review', args=[review.id]), follow=True)
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = add_store_review(request, store_id=review.id)
        self.assertEqual(response.status_code, 302)
