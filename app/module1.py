import logging
import sys

logger = logging.getLogger(__name__)
# set logging level for ENTIRE logger
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(filename)s:%(funcName)s - %(levelname)s - %(message)s"
)
# add formatter to chINFO
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


def func1() -> None:
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
