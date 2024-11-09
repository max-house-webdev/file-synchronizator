import time

import requests
from loguru import logger

from src.config.constant import INTERVAL
from src.config.get_env import get_env
from src.config.loguru import LOGGER_CONFIG
from src.config.set_local_dir_path import set_local_dir_path
from src.file_observer.FileObserver import FileObserver
from src.yandex_loader.CloudLoader import CloudLoader


def main():
    """Main entrypoint
    """
    # configure logger
    logger.configure(**LOGGER_CONFIG)
    # load environment variables
    env, env_error = get_env()

    if env_error is not None:
        logger.critical(env_error)

        return

    if env is None:
        logger.error(
            "Could not load environment variables. Expected dict and got None instead")

        return

    logger.debug("Environment variables loaded successfully")
    # successful start
    logger.info(
        "File synchronizer starts working")
    # set absolute path to local directory
    local_dir = set_local_dir_path(env["PARENT_DIR"])
    logger.debug(
        f"Local directory is '{local_dir}'")
    # todo: this works
    # session = requests.Session()

    # cloud_loader = CloudLoader(session, env["CLOUD_URL"], env["TOKEN"])

    # content, code = cloud_loader.get_resource_list()

    # logger.info(code)
    # logger.info(content)
    # todo: this works
    observer = FileObserver(local_dir)

    while observer.is_observing:
        observer.update_local_files_storage()
        logger.info(observer.local_files_storage)
        time.sleep(INTERVAL)

    logger.info("working")


if __name__ == "__main__":
    main()
