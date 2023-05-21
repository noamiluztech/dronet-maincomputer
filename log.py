# DroNet-2023
# Main Computer
import datetime
import os


# starting log faucntion

import logging

def configure_logger():

    # create the log directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    # get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    # Create the logger
    logger = logging.getLogger(f"data_run_{timestamp}")
    logger.setLevel(logging.DEBUG)

    # Create a file handler to save the log messages to the specified file
    log_file = f"logs/data_run_{timestamp}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter to specify the log message format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Set the formatter for the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger, log_file
