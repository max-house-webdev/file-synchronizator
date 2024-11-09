from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Tuple

import requests


@dataclass
class CloudLoaderAbstraction(ABC):
    """Cloud loader abstraction implementation

    use yandex disk api
    """

    TIMEOUT = 5

    def __init__(self,
                 session: requests.Session,
                 cloud_url: str,
                 token: str):

        self.__CLOUD_DIR = "app:/"

        self.__session = session
        self.__cloud_url = cloud_url
        self.__session = session

        self.__headers = {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {token}"
        }

    @property
    def CLOUD_DIR(self):
        """App cloud directory identifier

        used in uri
        """
        return self.__CLOUD_DIR

    @property
    def cloud_url(self):
        """Cloud base ur
        """
        return self.__cloud_url

    @property
    def session(self) -> requests.Session:
        """Request session
        """
        return self.__session

    @property
    def headers(self):
        """HTTP-headers
        """
        return self.__headers

    @abstractmethod
    def get_resource_list(self) -> Tuple[bytes | Any, int]:
        """Get resource list in app cloud directory
        """
