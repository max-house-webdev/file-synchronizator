import time

import requests

from src.config.constant import INTERVAL
from src.config.get_env import get_env
from src.config.set_local_dir_path import set_local_dir_path
from src.file_observer.FileObserver import FileObserver
from src.logger.log_messages import (APP_STARTED, APP_WORKING,
                                     COULD_NOT_LOAD_ENV,
                                     ENV_LOADED_SUCCESSFULLY, local_dir)
from src.logger.loguru_config import logger
from src.yandex_loader.CloudLoader import CloudLoader


def main():
    """Main entrypoint
    """
    # load environment variables
    env, env_error = get_env()

    if env_error is not None:
        logger.critical(env_error)

        return

    if env is None:
        logger.error(
            COULD_NOT_LOAD_ENV)

        return

    logger.debug(ENV_LOADED_SUCCESSFULLY)
    # successful start
    logger.info(
        APP_STARTED)

    logger.info("info")
    logger.error("error")
    logger.critical("critical")
    logger.exception("exception")

    # set absolute path to local directory
    local_dir_name = set_local_dir_path(env["PARENT_DIR"])
    logger.debug(local_dir(local_dir_name))
    # todo: this works
    # session = requests.Session()

    # cloud_loader = CloudLoader(session, env["CLOUD_URL"], env["TOKEN"])

    # content, code = cloud_loader.get_resource_list()

    # logger.info(code)
    # logger.info(content)
    # todo: this works
    observer = FileObserver(local_dir_name)

    while observer.is_observing:
        observer.update_local_files_storage()
        logger.info(observer.local_files_storage)
        time.sleep(INTERVAL)

    logger.info(APP_WORKING)


if __name__ == "__main__":
    main()
