from django.test import Client, TestCase
from django.urls import reverse


class TestHome(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.home_url = reverse('Dashboard:Home')
        self.home_section_url = reverse(
            'Dashboard:section',
            args=['Fruit']
        )
        self.product_filter_url = reverse('Dashboard:filter')

    def testHome(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Dashboard.html')

    def testSections(self):
        response = self.client.get(self.home_section_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePageSections.html')

    def testProductFilter(self):
        response = self.client.get(self.product_filter_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePageProduct.html')
