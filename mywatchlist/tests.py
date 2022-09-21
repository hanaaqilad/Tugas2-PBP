from audioop import reverse
from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class Test(TestCase):
    def test_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def test_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    # def test_html(self):
    #     client = Client()
    #     response = client.get(reverse("mywatchlist:show_html"))
    #     self.assertEqual(response.status_code,200)

    # def test_xml(self):
    #     client = Client()
    #     response = client.get(reverse("MyWatchList:show_xml"))
    #     self.assertEqual(response.status_code,200)

    # def test_json(self):
    #     client = Client()
    #     response = client.get(reverse("mywatchlist:show_json"))
    #     self.assertEqual(response.status_code,200)

    
