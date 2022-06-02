import unittest
import numpy as np
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)) + "/habittracker")
from calc_stats import calc_most_popular


class TestMorePopular(unittest.TestCase):

    def test_normal_matrix_1(self):
        ticks = np.array([[True, True, True], [False, True, True], [False, True, False]])
        result = calc_most_popular(ticks)
        assert np.all(result[0] == np.array([0])) and np.all(result[1] == np.array([1]))

    def test_normal_matrix_2(self):
        ticks = np.array([[True], [True], [False]])
        result = calc_most_popular(ticks)
        assert np.all(result[0] == np.array([0, 1])) and np.all(result[1] == np.array([0]))
        
    def test_one_dimension(self):
        ticks = np.array([True, False])
        result = calc_most_popular(ticks)
        assert result == (-1, -1)
        
    def test_empty_matrix(self):
        ticks = np.array([])
        result = calc_most_popular(ticks)
        assert result == (-1, -1)
        
    def test_string_input(self):
        ticks = np.array([['a'], ['b']])
        with self.assertRaises(np.core._exceptions._UFuncNoLoopError):
            calc_most_popular(ticks)
