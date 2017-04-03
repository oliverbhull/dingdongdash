from django.db import transaction

from django.contrib.auth.models import User
from django.test import Client, TestCase

from core.models import Button, ButtonAction, Phone


class PrimaryUseTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.create_user(username='User1',
                                              email='user1@test.com',
                                              password='abc123!@#')
        self.phone = Phone.objects.create(phone_number="+19783284466", user=self.user1)
        self.button = Button.objects.create(serial_number="fooofooodoggdogg")
        self.button.single_press_actions.add(
            ButtonAction.objects.create(type="call",
                                        name="Call User1",
                                        target_user=self.phone,
                                        message="Testing 123"))
        self.button.double_press_actions.add(
             ButtonAction.objects.create(type="message",
                                         name="Text User1",
                                         target_user=self.phone,
                                         message="Testing 123"))

    def tearDown(self):
        self.button.delete()

    def test_process_button_low_battery(self):
        response = self.client.post('/api/functions/process_button/', {
            'spoof': True,
            'batteryVoltage': [u'249mV'],
            'serialNumber': [u'fooofooodoggdogg'],
            'clickType': [u'SINGLE']
        })

        self.assertEquals(response.status_code, 200)

    def test_process_button_unknown(self):
        try:
            with transaction.atomic():
                self.client.post('/api/functions/process_button/', {
                    'spoof': True,
                    'batteryVoltage': [u'1546mV'],
                    'serialNumber': [u'1111222233334444'],
                    'clickType': [u'SINGLE']
                })
        except Exception:
            self.assertEquals(True, True)
            return

        self.fail()

    def test_process_button_single(self):
        response = self.client.post('/api/functions/process_button/', {
            'spoof': True,
            'batteryVoltage': [u'1546mV'],
            'serialNumber': [u'fooofooodoggdogg'],
            'clickType': [u'SINGLE']
        })

        self.assertEquals(response.status_code, 200)

    def test_process_button_double(self):
        response = self.client.post('/api/functions/process_button/', {
            'spoof': True,
            'batteryVoltage': [u'1546mV'],
            'serialNumber': [u'fooofooodoggdogg'],
            'clickType': [u'DOUBLE']
        })

        self.assertEquals(response.status_code, 200)

    def test_process_button_long(self):
        try:
            with transaction.atomic():
                self.client.post('/api/functions/process_button/', {
                    'spoof': True,
                    'batteryVoltage': [u'1546mV'],
                    'serialNumber': [u'fooofooodoggdogg'],
                    'clickType': [u'LONG']
                })
        except Exception:
            self.assertEquals(True, True)
            return

        self.fail()

    def test_non_post_request(self):
        response = self.client.get('/api/functions/process_button/', {})
        self.assertEquals(response.status_code, 400)
