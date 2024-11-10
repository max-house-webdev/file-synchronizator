
import time

import requests

from src.env_loader.EnvLoader import EnvLoader
from src.file_observer.FileObserver import FileObserver
from src.logger.logger import (APP_STARTED, APP_STOPPED, APP_STOPPED_IN_ERROR,
                               APP_WORKING, ENV_LOADED_SUCCESSFULLY, local_dir,
                               logger)
from src.yandex_loader.CloudLoader import CloudLoader


def main():
    """Main entrypoint
    """
    # load environment variables
    env = EnvLoader()

    if env.ERROR is not None:
        logger.exception(env.ERROR)
        logger.info(APP_STOPPED_IN_ERROR)

        return

    logger.debug(ENV_LOADED_SUCCESSFULLY)
    logger.info(
        APP_STARTED)
    logger.debug(local_dir(env.LOCAL_DIR_PATH))

    # todo: this works
    session = requests.Session()

    cloud_loader = CloudLoader(session, env.CLOUD_URL, env.TOKEN)

    content, code = cloud_loader.get_resource_list()

    logger.info(code)
    logger.info(content)

    observer = FileObserver(env.LOCAL_DIR_PATH)

    while observer.is_observing:
        observer.observe_local_files_storage()
        logger.info(observer.local_files_storage)
        logger.info(hash(repr(observer.local_files_storage)))
        time.sleep(env.PERIOD)

    logger.info(APP_WORKING)

    # this line should be last one
    logger.info(APP_STOPPED)


if __name__ == "__main__":
    main()
