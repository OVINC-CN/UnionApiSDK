#!/usr/bin/env python

from setuptools import setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ovinc_client",
    version="0.4.0b0",
    author="OVINC",
    url="https://www.ovinc.cn/",
    author_email="contact@ovinc.cn",
    description="A Tool for OVINC Union API",
    packages=[
        "ovinc_client",
        "ovinc_client.account",
        "ovinc_client.account.migrations",
        "ovinc_client.components",
        "ovinc_client.core",
        "ovinc_client.tcaptcha",
        "ovinc_client.trace",
    ],
    install_requires=[
        "django>=4,<5",
        "django_environ>=0.10.0,<1",
        "djangorestframework>=3.14.0,<4",
        "pymysql>=1,<2",
        "django-cors-headers>=4.6.0,<5",
        "pytz>=2022.4,<2025",
        "django-sslserver>=0.22,<1",
        "pyOpenSSL>=22.1.0,<25",
        "django-simpleui>=2023.8.28,<2025",
        "adrf<1",
        "channels>=4,<5",
        "redis>=5.0.0,<6",
        "django-redis>=5.0.0,<6",
        "python_json_logger>=2.0.3,<3",
        "httpx[http2]>=0.23.2,<1",
        "requests>=2.28.0,<3",
        "protobuf>=3.19.5,<6",
        "opentelemetry-api==1.29.0",
        "opentelemetry-sdk==1.29.0",
        "opentelemetry-exporter-otlp==1.29.0",
        "opentelemetry-instrumentation==0.50b0",
        "opentelemetry-instrumentation-asgi==0.50b0",
        "opentelemetry-instrumentation-django==0.50b0",
        "opentelemetry-instrumentation-dbapi==0.50b0",
        "opentelemetry-instrumentation-pymysql==0.50b0",
        "opentelemetry-instrumentation-redis==0.50b0",
        "opentelemetry-instrumentation-requests==0.50b0",
        "opentelemetry-instrumentation-celery==0.50b0",
        "opentelemetry-instrumentation-logging==0.50b0",
        "opentelemetry-instrumentation-httpx==0.50b0",
        "ipython>=8.10.0,<9",
        "tencentcloud-sdk-python>=3.0.785,<4",
        "pycryptodome>=3.20.0,<4",
        "pydantic>=2,<3",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
)
