"""
custom_logging.py
author: Harold Goldman
email: mikerah@gmail.com
06-07-2017

Module for custom logging format

usage:
    def setup_logs():
        return custom_logging.logger(config["logfile"], config["log_level"])

"""
import logging
from logging.handlers import RotatingFileHandler


def logger(logfile, level="DEBUG"):
    """
    Logger method for use by our python
    code sets up the log formatting and destination

    Parameters
    -------
    logfile : string
        Destination file for logs
    level : string
         Optional Logging Level, DEBUG is default

    Returns
    -------
    object
        Returns an instance of logger with our settings
    """

    logger = logging.getLogger("")
    logger.setLevel(level)
    fm =  """  %(levelname)s | %(asctime)s | pid:%(process)s | %(pathname)s:%(lineno)d | %(message)s """
    formatter = logging.Formatter(fm, "%Y-%m-%d %H:%M:%S")

    handler = RotatingFileHandler(logfile, maxBytes=10000000,
                                  backupCount=10)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
