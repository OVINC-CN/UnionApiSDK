import os

from asgiref.sync import async_to_sync

from tests.base import TestBase


class NoticeTest(TestBase):
    def test_send_robot(self):
        resp = async_to_sync(self.client.notice.robot)(
            {
                "robots": [os.getenv("UNION_API_WXROBOT")],
                "content": {"msgtype": "text", "text": {"content": "广州今日天气：29度，大部分多云，降雨概率：60%", "mentioned_list": []}},
            }
        )
        self.assertEqual(resp.data.get("message"), "success")
