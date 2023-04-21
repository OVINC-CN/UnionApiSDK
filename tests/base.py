import os
from unittest import TestCase

from ovinc_client import OVINCClient


class TestBase(TestCase):
    def setUp(self) -> None:
        self.client = OVINCClient(os.getenv("APP_CODE"), os.getenv("APP_SECRET"), os.getenv("API_URL"))
