from django.test import TestCase
from django.test import Client
from .models import Message


# Create your tests here.
class MessageTest(TestCase):
    def setUp(self):
        Message.objects.create(name="Lucy", content='Django入门')
        Message.objects.create(name='May', content='入门到放弃')

    def test_Message(self):
        info = Message.objects.get(name='Lucy')
        self.assertIsNotNone(info.timestamp)

    def test_post(self):
        c = Client()
        data = {
            'name': 'Tim',
            'content': '删库到跑路',
        }
        response = c.post('/', data=data)
        status_code = response.status_code
        info = Message.objects.get(name='Tim')

        # 判断测试用例的执行结果
        self.assertEquals(status_code, 302)
        self.assertEquals(info.content, '删库到跑路')
