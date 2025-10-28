"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=",")


def daily_mean(data):
    """Returns the mean values of an array of data

    Args:
        data (np.array): Array of the daily data

    Returns:
        np.array: array of mean values
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Returns the maximum values of an array of data

    Args:
        data (np.array): Array of the daily data

    Returns:
        np.array: array of max values
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Returns the minimum values of an array of data

    Args:
        data (np.array): Array of the daily data

    Returns:
        np.array: array of min values
    """
    return np.min(data, axis=0)
