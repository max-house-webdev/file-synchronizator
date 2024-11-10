"""Logger configuration
"""
import os
from sys import stderr, stdout
from typing import Any, Dict, Literal

from loguru import logger

LOG_DIR = "logs"

LOG_ALL = "synchronizer.log"
LOG_INFO = "synchronizer.info.log"

log_all_path = os.path.join(LOG_DIR, LOG_ALL)
log_info_path = os.path.join(LOG_DIR, LOG_INFO)

TKey = Literal["handlers"]


LOGGER_CONFIG: Dict[TKey, Any] = {
    "handlers": [
        {
            "sink": stderr or stdout,
            "format": "* synchronizer {time:HH:mm:ss}:\t{message}",
            "level": "INFO",
        },
        {
            "sink": log_all_path,
            "format": "{time}:\t[{level}]\t{message}",
            "level": "TRACE",
            "retention": "3 days"
        },
        {
            "sink": log_info_path,
            "format": "{time}:\t[{level}]\t{message}",
            "level": "INFO",
            "retention": "3 days"
        },
    ]
}

logger.configure(**LOGGER_CONFIG)
