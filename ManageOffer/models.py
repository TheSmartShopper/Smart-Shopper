from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from ManageProduct.models import Product
from ManageReview.models import Review


class Offer(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    expiratiDate = models.DateTimeField(default=datetime.now)
    state = models.BooleanField(default=False)
    name = models.CharField(max_length=50, blank=True)
    number_OF_Copy = models.PositiveIntegerField(default=0)
    price = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)
    image = models.ImageField(upload_to='Offers', default='package default.jpg')
    slug = models.SlugField(unique=True)
    review = models.ManyToManyField(Review, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Offer, self).save(*args, **kwargs)

    def __str__(self):
        # temp =datetime.date()
        # self.state = temp <= self.expiratiDate
        return self.name

    def average_review(self):
        revs = self.review.all()

        if revs:
            total = 0
            for x in revs:
                total += x.rating
            return (total / len(revs)) * 20
        else:
            return 0
