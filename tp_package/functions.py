"""
This module contains functions.
"""

import logging


logger = logging.getLogger(__name__)


def add_one(input_value):
    """
    This function adds 1 to the input value.
    """
    logger.info("tp_package.functions.add_one with input_value = %s", input_value)
    result = input_value+1
    logger.info("tp_package.functions.add_one result = %s", result)
    return result


def log_dummy(log_message: str = 'log_dummy default message.', log_severity: int = logging.DEBUG):
    """
    Intended for testing only.
    This function generates a log with a custom message and severity.
    """
    logger.log(log_severity, log_message)
