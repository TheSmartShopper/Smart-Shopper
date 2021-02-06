# Generated by Django 3.1.6 on 2021-02-06 22:02

import ManageStore.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ManageReview', '0001_initial'),
        ('ManageOffer', '0001_initial'),
        ('ManageProduct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AD_imags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ad_imags', models.ImageField(default='AD default.png', upload_to=ManageStore.models.AD_imags.AD_imags_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(default='store default.jpg', upload_to=ManageStore.models.Store.store_directory_path)),
                ('phonesNumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text="Phone number must be entered in the format '+999999999'. Up to 15 digits allowed.", max_length=128, null=True, region=None, unique=True)),
                ('type', models.CharField(choices=[('HyperMarket', 'HyperMarket'), ('BigMarket', 'BigMarket')], default='HyperMarket', max_length=50)),
                ('url', models.URLField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('start_hours', models.TimeField(blank=True, max_length=50, null=True)),
                ('close_hours', models.TimeField(blank=True, max_length=50, null=True)),
                ('state', models.BooleanField(blank=True, default=True)),
                ('join_at', models.DateField(blank=True, null=True)),
                ('new', models.BooleanField(default=True)),
                ('ADs', models.ManyToManyField(to='ManageStore.AD_imags')),
                ('StoreOffers', models.ManyToManyField(blank=True, to='ManageOffer.Offer')),
                ('StoreReviews', models.ManyToManyField(blank=True, to='ManageReview.Review')),
                ('products', models.ManyToManyField(blank=True, to='ManageProduct.Product')),
                ('sections', models.ManyToManyField(blank=True, to='ManageStore.Section')),
            ],
        ),
    ]
