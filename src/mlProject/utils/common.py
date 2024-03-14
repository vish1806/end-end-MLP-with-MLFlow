# Import necessary modules
import os  # Provides functions for interacting with the operating system
from box.exceptions import BoxValueError  # Exception for Box library
import yaml # Provides functions for working with YAML files
from mlProject import logger  # Import logger from mlProject module
import json  # Provides functions for working with JSON files
import joblib  # Provides functions for saving and loading binary files
from ensure import ensure_annotations  # Decorator for enforcing type annotations if int is given as type, then we cannot give another data type, only int
from box import ConfigBox  # Class for working with nested dictionaries, provides enhanced features for working with dictionaries in Python.
from pathlib import Path  # Provides functions for working with file paths
from typing import Any  # Type hint for Any type


# Define a function to read YAML files and return a ConfigBox object
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        # Open the YAML file
        with open(path_to_yaml) as yaml_file:
            # Load the YAML content
            content = yaml.safe_load(yaml_file)
            # Log a message indicating successful loading of the YAML file
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            # Return the YAML content as a ConfigBox object
            return ConfigBox(content)
    except BoxValueError:
        # Raise a ValueError if the YAML file is empty
        raise ValueError("yaml file is empty")
    except Exception as e:
        # Raise any other exceptions that occur during file reading
        raise e


# Define a function to create directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        # Create the directory if it doesn't exist
        os.makedirs(path, exist_ok=True)
        if verbose: 
            # verbose provides more info than what is needed
            # Log a message indicating successful directory creation
            logger.info(f"created directory at: {path}")


# Define a function to save data to a JSON file
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    # Write data to the JSON file
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    # Log a message indicating successful saving of the JSON file
    logger.info(f"json file saved at: {path}")


# Define a function to load data from a JSON file
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    # Read data from the JSON file
    with open(path) as f:
        content = json.load(f)

    # Log a message indicating successful loading of the JSON file
    logger.info(f"json file loaded succesfully from: {path}")
    # Return the loaded data as a ConfigBox object
    return ConfigBox(content)


# Define a function to save data to a binary file
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    # Save data to the binary file
    joblib.dump(value=data, filename=path)
    # Log a message indicating successful saving of the binary file
    logger.info(f"binary file saved at: {path}")


# Define a function to load data from a binary file
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    # Load data from the binary file
    data = joblib.load(path)
    # Log a message indicating successful loading of the binary file
    logger.info(f"binary file loaded from: {path}")
    # Return the loaded data
    return data


# Define a function to get the size of a file in KB
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    # Calculate the size of the file in KB
    size_in_kb = round(os.path.getsize(path) / 1024)
    # Return the size as a string
    return f"~ {size_in_kb} KB"
