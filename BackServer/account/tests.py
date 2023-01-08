from django.test import TestCase, Client
from .models import *
from .views import *


class UserTests(TestCase):
    def test_register(self):
        client = Client(enforce_csrf_checks=False)
        response = client.post('/account/register',
            data={
                'username': 'cocopalm',
                'gender': '0',
                'nickname': '한글도 되나?',
                'email': 'foo@bar.com',
                'password1': '1',
                'password2': '1',
            }
        ).json()
        self.assertEqual(response['result'], 'Successed')
