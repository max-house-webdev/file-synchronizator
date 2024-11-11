import pathlib
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class FileObserverAbstraction(ABC):
    """File observer abstraction implementation
    """

    local_dir: pathlib.Path
    is_observing: bool = True
    local_files_storage: Dict[str, float] = field(default_factory=dict)

    @abstractmethod
    def observe_local_files_storage(self):
        """ Update the dict storage of files in local directory
        """
