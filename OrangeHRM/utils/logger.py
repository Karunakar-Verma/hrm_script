import logging
import os

def get_logger():

    log_dir = "Logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "Orange.log")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger