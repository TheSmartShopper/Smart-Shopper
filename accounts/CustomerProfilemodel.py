from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from ManageProduct.models import Product
from ManageReview.models import Review
from ShoppingCart.models import ShoppingCart
from django.conf import settings


class CustomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='CustomerProfileImages', default='Customer default.png')
    address = models.CharField(max_length=100, null=False)
    join_at = models.DateTimeField(default=datetime.now)
    country = CountryField(default='Jordan')
    cart = models.OneToOneField(ShoppingCart, on_delete=models.SET_NULL, null=True, blank=True)
    favorite = models.ManyToManyField(Product, blank=True)
    review = models.ManyToManyField(Review, blank=True)

    class Meta:
        verbose_name_plural = 'Customer Profile'

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        if not self.cart:
            self.cart = ShoppingCart.objects.create()

        super(CustomerProfile, self).save(*args, **kwargs)

    def get_Customer_Favorite(self):
        return self.favorite.all()

    def get_Customer_Favorite_IDs(self):
        IDs = []
        for product in self.favorite.all():
            IDs.append(product.id)
        return IDs
