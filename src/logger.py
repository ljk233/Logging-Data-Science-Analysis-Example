"""logger.py

Module for custom logging to track the progress of linear regression analysis.
"""

import logging


def setup_logger():
    """Set up the logging configuration.

    This function configures the logging system with a specified format,
    log level, and output file.

    Returns:
        None
    """
    logging.basicConfig(
        filename="log.txt",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.info("Initialised new pipeline.")


def log_info(message):
    """Log an information message.

    Args:
        message (str): The information message to log.

    Returns:
        None
    """
    logging.info(message)


def log_error(message):
    """Log an error message.

    Args:
        message (str): The error message to log.

    Returns:
        None
    """
    logging.error(message)
