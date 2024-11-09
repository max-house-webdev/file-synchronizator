import os
from typing import Dict, Literal

from dotenv import load_dotenv

TKey = Literal["TOKEN"] | Literal["CLIENT_ID"] | Literal["CLOUD_URL"] | Literal["PARENT_DIR"]


def get_env():
    """Load environment variables
    """
    env: Dict[str, str] = {}
    load_dotenv()

    def load(key_: TKey):
        try:
            value = os.environ[key_]

            if value == "":
                raise KeyError(f"Environment variable {key_} is empty string")

            return os.environ[key_], None

        except KeyError as e:
            if key_ == "PARENT_DIR":

                return None, None

            return None, e

    keys = ("TOKEN", "CLIENT_ID", "CLOUD_URL", "PARENT_DIR")

    allowed_none = ("PARENT_DIR", )

    try:
        for key in keys:
            value, err = load(key)

            if err is not None:

                return None, err

            if value is None:
                if not key in allowed_none:
                    raise ValueError(f"Environment variable {key} is None")

                env |= {key: ""}

            else:
                env |= {key: value}

        return env, None

    except (KeyError, ValueError) as e:

        return None, e
