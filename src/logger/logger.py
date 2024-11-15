from loguru import logger

from src.logger.loguru_config import LOGGER_CONFIG

logger.configure(**LOGGER_CONFIG)
