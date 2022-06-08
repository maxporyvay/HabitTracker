import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from habittracker.gui import parse_tracker_input_file  # noqa: E402


class TestTrackerInput(unittest.TestCase):

    def test_normal_input_1(self):
        lines = ['August 2022\n', '0\n', '31\n']
        result = parse_tracker_input_file(lines)
        assert result == ('August 2022', 31, [], [])

    def test_normal_input_2(self):
        lines = ['July 2023\n', '2\n', '4\n', 'Jogging\n', 'Sleeping 8 hrs\n', '0\n', '0\n', '0\n', '1\n', '0\n', '1\n', '1\n', '0\n']
        result = parse_tracker_input_file(lines)
        assert result == ('July 2023', 4, ['Jogging', 'Sleeping 8 hrs'], [[False, False, False, True], [False, True, True, False]])

    def test_incorrect_input(self):
        lines = ['August 2022\n', '31\n']
        with self.assertRaises(ValueError):
            parse_tracker_input_file(lines)
