from django.test import TestCase
from .models import URL

class TestURL(TestCase):
    def setUp(self) -> None:
        URL.objects.create(url="http://www.google.com")
    
    def test_short_url(self):
        url = URL.objects.latest('created_date')
        assert url.short_url is not None
        assert len(url.short_url) == 7
    
    def test_create_url_invalid(self):
        response = self.client.post("/", {"url": ""})
        assert response.status_code == 400
        assert response.context[0]['errors']['url'].get_json_data()[0]['message'] == "This field is required."
    
    def test_create_url_valid(self):
        url = "http://www.google.com"

        response = self.client.post("/", {"url": url})

        url_obj = URL.objects.latest('created_date')

        assert response.status_code == 201
        self.assertEqual(url, response.context[0]['url'])
        self.assertEqual(
            f"http://testserver/{url_obj.short_url}", response.context[0]['short_url'])
