from typing import List

from .base_logger import BaseLogger


class MultiLogger(BaseLogger):
    """Logger that is formed of many loggers, each of them with its own level. Every message is sent to the different loggers.
    """
    def __init__(self, log_name: str, loggers: List[BaseLogger]):
        super(MultiLogger, self).__init__(log_name, 0)
        self._loggers = loggers

    def debug(self, msg: str):
        for logger in self._loggers:
            logger.debug(msg)

    def info(self, msg: str):
        for logger in self._loggers:
            logger.info(msg)

    def warning(self, msg: str):
        for logger in self._loggers:
            logger.warning(msg)

    def error(self, msg: str):
        for logger in self._loggers:
            logger.error(msg)

    def exception(self, msg: str):
        for logger in self._loggers:
            logger.exception(msg)
