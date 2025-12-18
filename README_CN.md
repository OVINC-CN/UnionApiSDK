# OVINC Union Api SDK

[![PyPI version](https://badge.fury.io/py/ovinc-client.svg)](https://badge.fury.io/py/ovinc-client)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

[English Docs](README.md)

OVINC Union API 的 Python 客户端，提供对认证、通知和 TCaptcha 验证的便捷访问。

## 安装

```bash
pip install ovinc-client
```

## 使用方法

### 初始化

```python
from ovinc_client.client import OVINCClient

APP_CODE = "your_app_code"
APP_SECRET = "your_app_secret"
OVINC_API_URL = "https://api.ovinc.cn"

client = OVINCClient(app_code=APP_CODE, app_secret=APP_SECRET, union_api_url=OVINC_API_URL)
```

### 通知 (Notice)

#### 发送邮件

```python
response = client.notice.mail({
    "usernames": ["user1", "user2"],
    "content": {
        "title": "Hello",
        "content": "This is a test email."
    }
})
print(response.data)
```

#### 发送短信

```python
response = client.notice.sms({
    "usernames": ["user1", "user2"],
    "content": {
        "tid": "123456",
        "params": ["1234"]
    }
})
print(response.data)
```

#### 发送机器人消息

```python
response = client.notice.robot({
    "robots": ["robot_id_1"],
    "content": {
        "msgtype": "text",
        "text": {
            "content": "Hello from robot"
        }
    }
})
print(response.data)
```

### 认证 (Auth)

#### 验证码校验

```python
response = client.auth.verify_code({
    "code": "123456",
    "key": "user_identifier"
})
print(response.data)
```

### TCaptcha 验证

此模块需要配置 Django settings。

**配置:**

```python
# settings.py
CAPTCHA_TCLOUD_ID = "your_tencent_cloud_id"
CAPTCHA_TCLOUD_KEY = "your_tencent_cloud_key"
CAPTCHA_APP_ID = "your_captcha_app_id"
CAPTCHA_APP_SECRET = "your_captcha_app_secret"
CAPTCHA_ENABLED = True
```

**使用:**

```python
from ovinc_client.tcaptcha.utils import TCaptchaVerify

# 在视图或 API 中
def verify_captcha(request):
    user_ip = request.META.get("REMOTE_ADDR")
    ticket = request.data.get("ticket")
    randstr = request.data.get("randstr")
    ret = request.data.get("ret")
    
    verifier = TCaptchaVerify(
        user_ip=user_ip,
        ticket=ticket,
        randstr=randstr,
        ret=ret
    )
    
    if verifier.verify():
        return "Success"
    else:
        return "Failed"
```

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。
