import os
from box import Box, BoxError  

import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations  # ✅ This is the actual decorator

from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Read a YAML file and return 
    Args:
        path_to_yaml (str): Path like input
        
    Raises:
        ValueError: If the YAML file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxError as e:
        raise ValueError(f"yaml file is empty")
        
    except Exception as e:
        raise e
    



@ ensure_annotations
def create_directories(path_to_directories:list,verbose: bool=True):
    """
    Create directories if they do not exist.
    Args:
        path_to_directories (list): List of directories to create
        verbose (bool): If True, print the creation of directories
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path:Path) ->str:
    """
    Get the size of a file in KB.
    Args:
        path (Path): path of  the file
    Returns:
        str:size in KB
    """
    size_in_Kb=round(os.path.getsize(path)/1024,2)
    return f"~{size_in_Kb} KB"
