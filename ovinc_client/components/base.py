import abc

from ovinc_client.constants import ResponseData


class Component:
    """
    Component
    """


class Endpoint:
    """
    Endpoint
    """

    def __init__(self, client, base_url: str):
        self._client = client
        self.base_url = base_url

    def __call__(self, params: dict) -> ResponseData:
        return self._client.call_api(method=self.method, url=self.url, params=params)

    @property
    def url(self) -> str:
        return self.base_url.rstrip("/") + "/" + self.path.lstrip("/")

    @property
    @abc.abstractmethod
    def method(self) -> str:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def path(self) -> str:
        raise NotImplementedError
