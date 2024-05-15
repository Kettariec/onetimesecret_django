from rest_framework.test import APITestCase, APIClient
from onetimesecret.models import Secret
from rest_framework import status


class SecretTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.secret = Secret.objects.create(text='test text')

    def test_create_secret(self):
        data = {
            "text": 'test text',
            "days": 3
        }
        response = self.client.post(
            'http://127.0.0.1:8000/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_no_secret(self):
        response = self.client.get(
            'http://127.0.0.1:8000/secret/test/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )
