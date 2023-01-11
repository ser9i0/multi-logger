import logging
import requests

from .base_logger import BaseLogger


class TelegramLogger(BaseLogger):
    """Send log messages to a Telegram chat bot, also to a
    backup logfile to avoid information loss because of a connection failure
    """
    def __init__(self, log_name: str, log_level: int, log_path: str = None):
        super(TelegramLogger, self).__init__(log_name, log_level)
        # CHANGE CHAT IDs AND BOT API BEFORE USING THIS CODE
        self._chat_ids = ['1111111', '2222222', '3333333', '4444444']
        self._base_url = 'https://api.telegram.org/botXXXYYYZZZ/'
        self._logfile = None

        if log_path is not None:
            self._logfile = logging.getLogger(log_name)
            self._logfile.setLevel(logging.DEBUG)

            """Create file handler with debug level"""
            fh = logging.handlers.RotatingFileHandler(filename=log_path,
                                                      maxBytes=4000000,
                                                      backupCount=256)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s"))
            self._logfile.addHandler(fh)

    def debug(self, msg: str):
        if self._log_level > 2:
            if self._logfile is not None:
                self._logfile.debug(msg)
            self._send_message(f"{self._log_name} - DEBUG: {msg}")

    def info(self, msg: str):
        if self._log_level > 1:
            if self._logfile is not None:
                self._logfile.info(msg)
            self._send_message(f"{self._log_name} - INFO: {msg}")

    def warning(self, msg: str):
        if self._log_level > 0:
            if self._logfile is not None:
                self._logfile.warning(msg)
            self._send_message(f"{self._log_name} - WARNING: {msg}")

    def error(self, msg: str):
        if self._log_level >= 0:
            if self._logfile is not None:
                self._logfile.error(msg)
            self._send_message(f"{self._log_name} - ERROR: {msg}")

    def exception(self, msg: str):
        if self._log_level >= 0:
            if self._logfile is not None:
                self._logfile.exception(msg)
            self._send_message(f"{self._log_name} - EXCEPTION: {msg}")

    def _send_message(self, msg: str):
        for _chat_id in self._chat_ids:
            request = self._base_url + f"sendMessage?chat_id={_chat_id}&text={msg}"
            response = requests.get(request)
