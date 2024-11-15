import time

from src.env_loader import EnvLoader
from src.file_observer import FileObserver
from src.logger import (APP_STARTED, APP_STOPPED, APP_STOPPED_IN_ERROR,
                        APP_WORKING, ENV_LOADED_SUCCESSFULLY, fs_logger,
                        local_dir)
from src.yandex_loader import CloudLoader


def main():
    """Main entrypoint
    """
    # load environment variables
    env = EnvLoader()

    if env.ERROR is not None:
        fs_logger.exception(env.ERROR)
        fs_logger.info(APP_STOPPED_IN_ERROR)

        return

    fs_logger.debug(ENV_LOADED_SUCCESSFULLY)
    fs_logger.info(
        APP_STARTED)
    fs_logger.debug(local_dir(env.LOCAL_DIR_PATH))

    cloud_loader = CloudLoader(
        cloud_url=env.CLOUD_URL,
        cloud_dir=env.CLOUD_DIR_NAME,
        _token=env.TOKEN)

    # todo: debug
    content, code = cloud_loader.get_resource_list()

    fs_logger.info(code)
    fs_logger.info(content)

    observer = FileObserver(env.LOCAL_DIR_PATH)

    while observer.is_observing:
        observer.observe_local_files_storage()
        fs_logger.info(observer.local_files_storage)
        fs_logger.info(hash(repr(observer.local_files_storage)))
        time.sleep(env.PERIOD)

    fs_logger.info(APP_WORKING)

    # this line should be last one
    fs_logger.info(APP_STOPPED)


if __name__ == "__main__":
    main()
