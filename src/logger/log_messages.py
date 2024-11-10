from pathlib import Path

# app logs
APP_STARTED = "File synchronizer has started working"
APP_WORKING = "File synchronizer is working"
APP_STOPPED_IN_ERROR = "File synchronizer has been stopped in error"
APP_STOPPED = "File synchronizer has been stopped"
# loading env
ENV_LOADED_SUCCESSFULLY = "Environment variables loaded successfully"


def local_dir(dir_name: Path):
    "Logger message"
    return f"Local directory is '{dir_name}'"
