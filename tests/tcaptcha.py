from asgiref.sync import async_to_sync

from tests.base import TestBase


class TCaptchaTest(TestBase):
    def test_verify_ticket(self):
        resp = async_to_sync(self.client.tcaptcha.verify_ticket)({"user_ip": "127.0.0.1"})
        self.assertEqual(resp.data.get("data"), False)
