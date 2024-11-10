from typing import Dict


# todo:
class Connector():

    def __init__(self):
        self.__local_hash = 0
        self.__cloud_hash = 0
        self.local_need_udate

    @property
    def local_hash(self):
        """Local file storage hash
        """
        return self.__local_hash

    @local_hash.setter
    def local_hash(self, new_hash: int):
        self.__local_hash = new_hash

    @property
    def cloud_hash(self):
        """Cloud file storage hash
        """
        return self.__cloud_hash

    @cloud_hash.setter
    def cloud_hash(self, new_hash: int):
        self.__cloud_hash = new_hash

    def check_local_hash(self, local_files: Dict[str, float]):
        pass
