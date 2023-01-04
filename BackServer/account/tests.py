from django.test import TestCase
from .models import *
from .views import *
import json
from django.core.handlers.wsgi import WSGIRequest
from io import StringIO
from django.http import QueryDict


class Request:
    def __init__(self, method, POST) -> None:
        self.method = method
        self.POST = POST

class UserTests(TestCase):
    def test_user_integrity(self):
        """
        사용자 생성이 제대로 작동하는가
        """
        # 'username=user&gender=1&nickname=한글도 되나?&password1=1&password2=1&email=foo@bar.com',
        test_payloads = [
            {
                'username'  : 'user',
                'gender'    : '1',
                'nickname'  : '한글도 되나?',
                'password1' : '1',
                'password2' : '1',
                'email'     : 'foo@bar.com',
            },
        ]
        expected_reponses = [
            'Success',
        ]


        for expected_reponse, payload in zip(expected_reponses, test_payloads):
            # request = WSGIRequest({'REQUEST_METHOD':'POST', 'wsgi.input': StringIO()})
            # request.POST = QueryDict(payload, mutable=True)

            request = Request('POST', payload)
            response = json.loads(register(request).content)

            self.assertEqual(response['result'], expected_reponse)
        
    # def test_creation_charactor(self):
    #     '''
    #     캐릭터 및 인벤토리가 정상적으로 생성되는가
    #     '''

