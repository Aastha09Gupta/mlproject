import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
import dill


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        logging.error("Error occurred while saving object")
        raise CustomException("Error occurred while saving object", sys) from e