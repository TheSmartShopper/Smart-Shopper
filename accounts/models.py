from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from ManageStore.models import Store
from ShoppingCart.models import ShoppingCart


class StoreAdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='StoreAdminProfileImages',
                              default='Customer default.png')
    address = models.CharField(max_length=100, blank=True, null=True)
    join_at = models.DateTimeField(default=datetime.now)
    country = CountryField(default='Jordan')
    store = models.OneToOneField(Store, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Store Admin Profile'

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        if not self.store:
            self.store = Store.objects.create()
        super(StoreAdminProfile, self).save(*args, **kwargs)

    @property
    def get_slug(self):
        return self.slug

    def get_store_products_IDs(self):
        IDs = []
        for product in self.store.products.all():
            IDs.append(product.id)
        return IDs

    def get_store_offer_IDs(self):
        IDs = []
        for offer in self.store.StoreOffers.all():
            IDs.append(offer.id)
        return IDs


