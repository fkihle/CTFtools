import logging
from Templates.logging_colour import CustomFormatter

def create_logger(level):
    # Create custom logger
    logger = logging.getLogger(__name__)

    # Define format for logs
    fmt = '%(asctime)s | %(levelname)8s | %(name)s | %(message)s'

    # Create stdout handler for logging to the console
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(CustomFormatter(fmt))

    # Add both handlers to the logger
    logger.addHandler(stdout_handler)
    if level == 'INFO':
        logger.setLevel(logging.INFO)
    elif level == 'WARNING':
        logger.setLevel(logging.WARNING)
    elif level == 'ERROR':
        logger.setLevel(logging.ERROR)
    elif level == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)
    else:
        logger.setLevel(logging.DEBUG)

    return logger