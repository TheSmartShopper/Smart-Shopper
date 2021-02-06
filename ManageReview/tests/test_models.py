from unittest import TestCase

from ManageReview.models import Review


class TestReview(TestCase):
    def test_save(self):
        review = Review.objects.create(
            text='Review Text',
            rating=4
        )

        review.save()

        self.assertTrue(isinstance(review, Review))
