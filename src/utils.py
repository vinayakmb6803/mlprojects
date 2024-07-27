import os
import sys

import dill
# we can call from here to any py file
import numpy as np
import pandas as np


from src.exception import CustomExecption


def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)


        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomExecption(e,sys)
    

