from pathlib import Path

COULD_NOT_LOAD_ENV = "Could not load environment variables. Expected dict and got None instead"

ENV_LOADED_SUCCESSFULLY = "Environment variables loaded successfully"

APP_STARTED = "File synchronizer has started working"

APP_WORKING = "File synchronizer is working"


def local_dir(dir_name: Path):
    "Logger message"
    return f"Local directory is '{dir_name}'"
