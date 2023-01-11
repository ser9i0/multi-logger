from abc import ABCMeta, abstractmethod


class BaseLogger(metaclass=ABCMeta):
    """BaseLogger
    Abstract class for loggers
    """

    def __init__(self, log_name: str, log_level: int):
        self._log_name = log_name
        self._log_level = log_level

    @abstractmethod
    def debug(self, msg: str):
        raise NotImplementedError(
            "Should implement debug()"
        )

    @abstractmethod
    def info(self, msg: str):
        raise NotImplementedError(
            "Should implement info()"
        )

    @abstractmethod
    def warning(self, msg: str):
        raise NotImplementedError(
            "Should implement warning()"
        )

    @abstractmethod
    def error(self, msg: str):
        raise NotImplementedError(
            "Should implement error()"
        )

    @abstractmethod
    def exception(self, msg: str):
        raise NotImplementedError(
            "Should implement exception()"
        )
