from unittest import TestCase

from ManageReview.forms import ReviewForm


class TestReviewForm(TestCase):
    def test_valid_form(self):
        form = ReviewForm(
            data={
                'text': 'Review Text.',
                'rating': 1
            }
        )

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ReviewForm(data={})

        self.assertFalse(form.is_valid())
