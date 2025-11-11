from unittest.mock import Mock
from inflammation.compute_data import analyse_data
import numpy as np

def test_analyze_data():
    data_source = Mock()
    data_source.return_value = np.array([[[0, 2, 0]],
              [[0, 1, 0]]])
    analyse_data(data_source)