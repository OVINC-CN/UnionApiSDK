import os

from tests.base import TestBase


class NoticeTest(TestBase):
    def test_send_robot(self):
        resp = self.client.notice.robot(
            {
                "robots": [os.getenv("UNION_API_WXROBOT")],
                "content": {"msgtype": "text", "text": {"content": "广州今日天气：29度，大部分多云，降雨概率：60%", "mentioned_list": []}},
            }
        )
        self.assertTrue(resp.result)
        self.assertEqual(resp.data.get("message"), "success")
