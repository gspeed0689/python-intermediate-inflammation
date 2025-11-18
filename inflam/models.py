"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
from typing import Union

def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')

valid_numpy_methods = Union[np.mean, np.max, np.min, np.std, np.median]

def daily_statistic(data, method: valid_numpy_methods=np.mean):
    """Calculates a statistic on an Array using a numpy array statistic method. 

    Args:
        data (Array): 2D inflammation array
        method (valid_numpy_methods, optional): A numpy statistic method that does 
                not require any other arguments than the array and axis. 
                Defaults to np.mean.

    Returns:
        Array: A statistic in an array. 
    """
    return method(data, axis=0)
