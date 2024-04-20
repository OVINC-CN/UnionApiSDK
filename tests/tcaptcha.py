from tests.base import TestBase


class TCaptchaTest(TestBase):
    def test_verify_ticket(self):
        resp = self.client.tcaptcha.verify_ticket({"user_ip": "127.0.0.1"})
        self.assertEqual(resp.data.get("data"), False)
