from unittest import TestCase
from django.urls import reverse, resolve
from Dashboard.views import Home, section, productsfilter


class TestUrls(TestCase):
    def testHome(self):
        url = reverse('Dashboard:Home')
        self.assertEquals(resolve(url).func, Home)

    def testHomeSection(self):
        url = reverse('Dashboard:section', args=['Fruit'])
        self.assertEquals(resolve(url).func, section)

    def testProductFilter(self):
        url = reverse('Dashboard:filter')
        self.assertEquals(resolve(url).func, productsfilter)
