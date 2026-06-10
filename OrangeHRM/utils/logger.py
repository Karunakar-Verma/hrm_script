import logging
from logging import FileHandler


location = r"OrangeHRM\Logs\Orange.log"
def get_logger():
    logger = logging.getLogger("OrangeHRM")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(location)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger