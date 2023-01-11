import logging
import logstash

from .base_logger import BaseLogger


class BasicLogger(BaseLogger):
    """Mixed logger that implements both file and console logs
    """
    def __init__(self, log_name: str, log_level: int, log_path: str = None, console: bool = True):
        super(BasicLogger, self).__init__(log_name, log_level)
        self._logger = logging.getLogger(log_name)
        self._logger.setLevel(logging.DEBUG)

        if self._logger.hasHandlers():
            self._logger.handlers.clear()

        if log_path is None and console is False:
            raise Exception("Error creating BasicLogger logger: You must provide a log path or enable console log (or both).")

        if log_path:
            """Create file handler and set level"""
            fh = logging.handlers.RotatingFileHandler(filename=log_path,
                                                      maxBytes=4000000,
                                                      backupCount=256)
            if log_level == 3:
                fh.setLevel(logging.DEBUG)
            else:
                fh.setLevel(logging.INFO)
            fh.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s"))
            self._logger.addHandler(fh)

        if console:
            """Create console handler and set level"""
            ch = logging.StreamHandler()
            if log_level == 3:
                ch.setLevel(logging.DEBUG)
            else:
                ch.setLevel(logging.INFO)
            ch.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s"))
            self._logger.addHandler(ch)

    def add_logstash(self, tags, message_type: str, elk_server: str, port: int, version: int = 1):
        logstash_handler = logstash.TCPLogstashHandler(elk_server, port=port, version=version,
                                                       message_type=message_type, tags=tags)

        self._logger.addHandler(logstash_handler)

    def debug(self, msg: str):
        if self._log_level > 2:
            self._logger.debug(msg)

    def info(self, msg: str):
        if self._log_level > 1:
            self._logger.info(msg)

    def warning(self, msg: str):
        if self._log_level > 0:
            self._logger.warning(msg)

    def error(self, msg: str):
        if self._log_level >= 0:
            self._logger.error(msg)

    def exception(self, msg: str):
        if self._log_level >= 0:
            self._logger.exception(msg)
