"""Module containing mechanism for calculating standard deviation between datasets.
"""

import pathlib
import os
import numpy as np
from abc import abstractmethod, ABC

from inflammation import models, views


def analyse_data(data: np.array):
    """Calculates the standard deviation across days from a dataset. 

    Args:
        data (np.array): data array object loaded from a DataSource (CSVDataSource) and the .load_data() method. 
    """
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)

def load_csv_data(data_dir, filename_template='inflammation*.csv'):
    path = pathlib.Path(data_dir)
    CSVs = list(path.rglob(filename_template))
    if len(CSVs) == 0:
        raise ValueError("No CSVs found.")
    data = map(models.load_csv, CSVs)
    return data

class DataSource(ABC):
    @abstractmethod
    def load_data():
        pass

class CSVDataSource(DataSource):
    def __init__(self, data_dir, filename_template='inflammation*.csv'):
        self.data_dir = pathlib.Path(data_dir)
        self.filename_template = filename_template
    def load_data(self):
        CSVs = list(self.data_dir.rglob(self.filename_template))
        data = map(models.load_csv, CSVs)
        return data