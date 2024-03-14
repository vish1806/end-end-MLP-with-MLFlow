# Import necessary modules
import os  # Provides functions for interacting with the operating system
import sys  # Provides access to some variables used or maintained by the Python interpreter
import logging  # Provides a flexible framework for emitting log messages from Python programs

# Define a format string for log messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Specify the directory where log files will be stored
log_dir = "logs"

# Construct the full path to the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Set the format of log messages
    handlers=[  # Specify the handlers for log messages
        logging.FileHandler(log_filepath),  # Log messages to a file specified by log_filepath
        logging.StreamHandler(sys.stdout)  # Log messages to the standard output (console)
    ]
)

# Create a logger with the name "mlProjectLogger"
logger = logging.getLogger("mlProjectLogger")
