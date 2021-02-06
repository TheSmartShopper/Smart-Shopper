import datetime

from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

from ManageOffer.models import Offer
from ManageProduct.models import Product
from ManageReview.models import Review

STORE_TYPE = (
    ('HyperMarket', 'HyperMarket'),
    ('BigMarket', 'BigMarket')
)


class Section(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.name)


class AD_imags(models.Model):

    def AD_imags_directory_path(instance, filename):
        return 'AD_imags/{0}/{1}'.format(instance.name, filename)

    name = models.CharField(max_length=50)
    ad_imags = models.ImageField(upload_to=AD_imags_directory_path, default='AD default.png')


class Store(models.Model):
    def store_directory_path(instance, filename):
        return 'Store/{0}-{1}'.format((instance.name, instance.id), filename)

    sections = models.ManyToManyField(Section, blank=True)
    slug = models.SlugField(blank=True, null=True)
    name = models.CharField(max_length=50, unique=True, null=False)
    image = models.ImageField(upload_to=store_directory_path, default='store default.jpg')
    phonesNumber = PhoneNumberField(null=True, blank=True, unique=True,
                                    help_text='Phone number must be entered in the format \'+999999999\'. Up to 15 digits allowed.')
    type = models.CharField(max_length=50, choices=STORE_TYPE, default='HyperMarket')
    url = models.URLField(max_length=200, blank=True, unique=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    start_hours = models.TimeField(max_length=50, blank=True, null=True)
    close_hours = models.TimeField(max_length=50, blank=True, null=True)
    state = models.BooleanField(default=True, blank=True)
    join_at = models.DateField(null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    StoreReviews = models.ManyToManyField(Review, blank=True)
    StoreOffers = models.ManyToManyField(Offer, blank=True)
    new = models.BooleanField(default=True, null=False)
    ADs = models.ManyToManyField(AD_imags)

    def get_ADs_id(self):
        IDs = []
        for ad in self.ADs.all():
            IDs.append(ad.id)
        return IDs

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = ('NO NAME {0}'.format(datetime.datetime.now()))
        if not self.slug:
            self.slug = slugify(self.name)
        # if not self.ADs:
        #     self.ADs= AD_imags.objects.create(mane='{0}-{1}'.format(self.name,self.id))
        super(Store, self).save(*args, **kwargs)

    @property
    def is_open_now(self):
        if (self.close_hours and self.start_hours) is not None:
            now = datetime.datetime.now().time()
            self.state = self.start_hours <= now <= self.close_hours
            return self.state

    def __str__(self):
        self.is_open_now
        return str(self.name)

    @property
    def Average(self):
        if self.StoreReviews.all():
            revs = self.StoreReviews.all()
            total = 0
            for x in revs:
                total += x.rating
            return total / len(revs)
        else:
            return 0

    def get_sections(self):
        return self.sections.all()

    def is_sections_exist(self, sec):
        for name in self.sections.all():
            if name.name == sec:
                return True
        return False

    def add_sections(self, new_sections):
        sec = Section(name=new_sections)
        sec.save()
        self.sections.add(sec)
        self.save()
