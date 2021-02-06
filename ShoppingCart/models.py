from datetime import datetime

from django.db import models

from ManageOffer.models import Offer
from ManageProduct.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    added_at = models.DateTimeField(auto_now=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        if self.product:
            return str(self.product)
        else:
            return '#'


class CartOffer(models.Model):
    Offer = models.OneToOneField(Offer, on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        if self.Offer:
            return str(self.Offer)
        else:
            return '#'


class ShoppingCart(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    is_finished_adding = models.BooleanField(default=False)
    items = models.ManyToManyField(CartItem, blank=True)
    offers = models.ManyToManyField(CartOffer, blank=True)

    def save(self, *args, **kwargs):
        super(ShoppingCart, self).save(*args, **kwargs)

    def __str__(self):
        return '{0} - {1}'.format(super(ShoppingCart, self).__str__(), str(self.created_at)[:16])

    def get_cart_total(self):
        items = []
        for a in self.items.all():
            items.append(a.product.price * a.quantity)
        for a in self.offers.all():
            items.append(a.Offer.price * a.quantity)
        return sum(items)

    def get_product_ids(self):
        items = []
        for a in self.items.all():
            items.append(a.product.id)
        return items

    def get_offer_ids(self):
        items = []
        for a in self.offers.all():
            items.append(a.product.id)
        return items

    def add_product_to_cart(self, pro_id, quantity):
        new = CartItem.objects.create(
            product_id=pro_id,
            quantity=quantity
        )
        self.items.add(new)
        self.save()

    class Meta:
        ordering = ['id']
