"""Logger configuration
"""

import os
from sys import stderr, stdout
from typing import Any, Dict, Literal

LOG_FILE = "synchronizer.log"
LOG_INFO = "synchronizer.info.log"
LOG_DIR = "logs"

log_path = os.path.join(LOG_DIR, LOG_FILE)
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
            "sink": log_path,
            "format": "{time}\t[{level}]\t{message}",
            "level": "TRACE",
            "retention": "3 days"
        },
        {
            "sink": log_info_path,
            "format": "{time}:\t{message}",
            "level": "INFO",
            "retention": "3 days"
        }
    ]
}
