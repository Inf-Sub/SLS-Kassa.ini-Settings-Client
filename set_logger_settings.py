import config
import logging
from create_logging_dir import *


if make_log_dir():
    print(f'Make Log Dir: {config.LOGGER_DIR}')


# получение пользовательского логгера
py_logger = logging.getLogger(__name__)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler(f"{config.LOGGER_FILE}.log", mode='a')
py_formatter = logging.Formatter(f"{config.LOGGER_FORMAT}")

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)

# установка уровня логирования
if config.LOGGER_LEVEL == "info":
    py_logger.setLevel(logging.INFO)
    py_logger.info(f"setLevel: logging.INFO")
    DEBUG = False
elif config.LOGGER_LEVEL == "debug":
    py_logger.setLevel(logging.DEBUG)
    py_logger.info(f"setLevel: logging.DEBUG")
    DEBUG = True
else:
    DEBUG = False

py_logger.debug(f"Loading module {__name__}...")


def ln() -> str:
    return f"\n{'=' * 30}"


if config.LOGGER_LEVEL:
    print(f"{ln()}\nLog Level is: {config.LOGGER_LEVEL}{ln()}")
    if DEBUG:
        print(f"Debug Mode is: {DEBUG}{ln()}")
