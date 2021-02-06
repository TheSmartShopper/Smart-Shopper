from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from ManageReview.models import Review

SECTIONS = (
    ('Fruit', 'Fruit'),
    ('Veggies', 'Veggies'),
    ('Seafood', 'Seafood'),
    ('Meat', 'Meat'),
    ('Cereal', 'Cereal'),
    ('Condiments', 'Condiments'),
    ('Baby', 'Baby'),
    ('Pet', 'Pet'),
    ('Paper', 'Paper'),
    ('Dairy', 'Dairy'),
    ('Frozen', 'Frozen')
)

TYPE = (
    ('anonymous', 'anonymous'),
    ('Fresh Food', 'Fresh Food'),
    ('Food Cupboard', 'Food Cupboard'),
    ('Frozen Food', 'Frozen Food'),
    ('Beverages', 'Beverages'),
    ('Bio & Organic Food', 'Bio & Organic Food'),
    ('Baby Product', 'Baby Product'),
    ('Cleaning & Household', 'Cleaning & Household'),
    ('Health & Fitness', 'Health & Fitness'),
    ('Smartphones, Tablets & Wearables', 'Smartphones, Tablets & Wearables'),
    ('Electronics & Appliances', 'Electronics & Appliances'),
    ('Home & Garden', 'Home & Garden'),
    ('Pet Supplies ', 'Pet Supplies '),
    ('Toys & OutDoor', 'Toys & OutDoor'),
    ('Stationery & School Supplies', 'Stationery & School Supplies'),
    ('Kiosk', 'Kiosk'),
    ('Automotive', 'Automotive'),
)
MANUFACTURERS = (
    ('Manufacturer 1', 'Manufacturer 1'),
    ('Manufacturer 2', 'Manufacturer 2')
)

choices = SECTIONS


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    product_sections = models.CharField(max_length=50 ,blank=False)
    slug = models.SlugField(blank=True, null=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)], default=1.0)
    type = models.CharField(max_length=50, null=False, choices=TYPE)
    number_Of_Copy = models.PositiveIntegerField(blank=True, null=True)
    par_Code = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, choices=MANUFACTURERS, default='anonymous Manufacturer')
    # image = ResizedImageField(size=[662, 654], upload_to='Product/img/%Y-%m-%d/', default='Product default.png')
    image = models.ImageField(upload_to='Products', default='Product default.png')
    discount = models.FloatField(validators=[MinValueValidator(0.0)], default=1.0)
    ProductReview = models.ManyToManyField(Review, blank=True)

    class Meta:
        ordering = ["price"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.price:
            self.price = (self.price * self.discount)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        self.price = self.price * self.discount
        return str(self.name)

    @property
    def average_review(self):
        revs = self.ProductReview.all()

        if revs:
            total = 0
            for x in revs:
                total += x.rating
            return (total / len(revs)) * 20
        else:
            return 0

    def grt_price_after_discount(self):
        return self.price - (self.discount / 100 * self.price)
