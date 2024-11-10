from loguru import logger

from src.logger.log_messages import (APP_STARTED, APP_STOPPED,
                                     APP_STOPPED_IN_ERROR, APP_WORKING,
                                     ENV_LOADED_SUCCESSFULLY, local_dir)
from src.logger.loguru_config import LOGGER_CONFIG

logger.configure(**LOGGER_CONFIG)

__all__ = ["APP_STARTED", "APP_STOPPED",
           "APP_STOPPED_IN_ERROR", "APP_WORKING",
           "ENV_LOADED_SUCCESSFULLY", "local_dir"]
