import pathlib
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass
class FileObserverAbstraction(ABC):
    """File observer abstraction implementation
    """

    def __init__(self,
                 local_dir: pathlib.Path):
        self.__local_dir = local_dir
        self.__is_observing = True

        self.local_files_storage: Dict[str, float] = {}

    @property
    def local_dir(self) -> pathlib.Path:
        """Absolute path to local directory
        """
        return self.__local_dir

    @property
    def is_observing(self) -> bool:
        """Flag

        if True should observe local directory
        stop observing otherwise
        """
        return self.__is_observing

    @is_observing.setter
    def is_observing(self, is_observing: bool):
        self.__is_observing = is_observing

    @abstractmethod
    def update_local_files_storage(self):
        """ Update the dict storage of files in local directory
        """
