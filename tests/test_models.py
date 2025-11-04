"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max_integers():
    """Test the max function works for an array of integers.""" 
    
    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([5, 6])

    # Assert the test
    npt.assert_array_equal(daily_max(test_input), test_result)

def test_daily_min_integers():
    """Test the max function works for an array of integers.""" 
    
    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([1, 2])

    # Assert the test
    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_string():
    """Test the daily_min function that if it is passed a string a TypeError is raised."""
    with pytest.raises(TypeError):
        test_input = [["Empty", "Coconuts"], ["European Swallow", "African Swallow"]]
        error_expected = daily_min(test_input)