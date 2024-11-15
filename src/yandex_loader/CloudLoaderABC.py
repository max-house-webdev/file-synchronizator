from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Tuple

import requests


@dataclass
class CloudLoaderABC(ABC):
    """Cloud loader abstraction

    use yandex disk api
    """

    TIMEOUT = 5

    cloud_url: str
    cloud_dir: str
    _token: str
    session = requests.Session()

    @property
    def headers(self):
        """HTTP-headers
        """
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"OAuth {self._token}"
        }

    @abstractmethod
    def get_resource_list(self) -> Tuple[bytes | Any, int]:
        """Get resource list in app cloud directory
        """
