import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv

TKey = Literal["TOKEN"] | \
    Literal["CLOUD_URL"] | \
    Literal["CLOUD_DIR_NAME"] | \
    Literal["LOCAL_DIR_PATH"] | \
    Literal["SYNCHRONIZATION_PERIOD"]


class EnvLoader():
    """Environment variables loader
    """

    DEFAULT = "DEFAULT"

    def __init__(self):

        self.__token: str = ""
        self.__cloud_url: str = ""
        self.__cloud_dir_name: str = ""

        self.__local_dir_name = "local_dir"
        self.__local_dir_path: Path = Path.cwd().absolute().joinpath(self.__local_dir_name)

        self.__period = 0

        self.__error: KeyError | ValueError | None = None

        self.__load_env()

    @property
    def TOKEN(self):
        """Token
        """
        return self.__token

    @property
    def CLOUD_URL(self):
        """Cloud URL
        """
        return self.__cloud_url

    @property
    def CLOUD_DIR_NAME(self):
        """Cloud directory
        """
        return self.__cloud_dir_name

    @property
    def LOCAL_DIR_PATH(self):
        """Absolute path to local directory
        """
        return self.__local_dir_path

    @property
    def PERIOD(self):
        """Synchronization period
        """
        return self.__period

    @property
    def ERROR(self):
        """Raised error
        """
        return self.__error

    def __load(self, key_: TKey):
        try:
            value = os.environ[key_]

            if value == "" or \
                    value.strip().upper() == "NONE" or \
            value.strip().upper() == self.DEFAULT:
                if key_ == "LOCAL_DIR_PATH":

                    return self.DEFAULT, None

                raise KeyError(
                    f"Environment variable '{key_}' is empty string or None")

            return os.environ[key_], None

        except KeyError as e:
            self.__error = KeyError(
                f"Environment variable {e} is undefined")

            return None, self.__error

    def __load_env(self):
        load_dotenv()

        keys = ("TOKEN", "CLOUD_URL", "CLOUD_DIR_NAME", "LOCAL_DIR_PATH",
                "SYNCHRONIZATION_PERIOD")

        try:
            for key in keys:
                value, err = self.__load(key)

                if err is not None:

                    self.__error = err

                    return

                if value is None:
                    raise ValueError(f"Environment variable {key} is None")

                if key == "TOKEN":
                    self.__token = value

                elif key == "CLOUD_URL":
                    self.__cloud_url = value

                elif key == "CLOUD_DIR_NAME":
                    self.__cloud_dir_name = value

                elif key == "LOCAL_DIR_PATH":
                    self.__set_local_dir_path(value)

                elif key == "SYNCHRONIZATION_PERIOD":
                    self.__period = int(value)

        except (KeyError, ValueError) as e:
            self.__error = e

    def __set_local_dir_path(self, path_: str) -> None:
        if path_ == self.DEFAULT:

            return

        dirs = path_.split("/")
        local_dir_path = Path.home().absolute().joinpath(*dirs)

        if local_dir_path.exists():
            self.__local_dir_path = local_dir_path

            return

        Path(local_dir_path).mkdir(parents=True, exist_ok=True)
        self.__local_dir_path = local_dir_path
