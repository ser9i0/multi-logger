from multi_logger import MultiLogger, TelegramLogger, BasicLogger
from pathlib import Path


def create_logger():
    # Create log folder
    ROOT_PATH = Path(__file__).parent.resolve()
    LOG_PATH = ROOT_PATH / "logs"
    LOG_PATH.mkdir(exist_ok=True, parents=True)

    app_name = "mytestapp_v1"
    environment = "develop"

    log_name = f"{app_name}_{environment}"
    log_path = LOG_PATH / f"{log_name}.log"

    # Create loggers
    basic_logger = BasicLogger(log_name=log_name, log_path=log_path, 
                               log_level=3, console=True)
    basic_logger.add_logstash(tags=['mytestapp', 'v1', environment],
                              message_type=log_name, elk_server=ELK_SERVER_HOST, 
                              port=ELK_SERVER_PORT, version=1)
    loggers = [basic_logger]

    telegram_logger = TelegramLogger(log_name=log_name, log_level=0)
    loggers.append(telegram_logger)

    # Create MultiLogger
    logger = MultiLogger(log_name=log_name, loggers=loggers)

    return logger


if __name__ == "__main__":
    logger = create_logger()
    
    logger.info("This is an INFO message.")
    logger.debug("This is a DEBUG message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")
