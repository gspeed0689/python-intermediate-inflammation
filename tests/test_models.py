"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_statistic

@pytest.mark.parametrize(
    "test, method, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], np.mean, [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], np.mean, [3, 4]),
        ([ [0, 0], [0, 0], [0, 0] ], np.min, [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], np.min, [1, 2]),
        ([ [0, 0], [0, 0], [0, 0] ], np.max, [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], np.max, [5, 6]),
    ])
def test_method_expected(test, method, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(daily_statistic(np.array(test), method), np.array(expected))
