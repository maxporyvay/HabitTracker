import unittest
import sys
import os
import shutil
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from habittracker.gui import add_text_in_file  # noqa: E402


class TestPlansAdding(unittest.TestCase):

    def test_insert_info(self):
        filepath = os.path.dirname(__file__) + '/test_insert_input_plans.txt'
        newfilepath = os.path.dirname(__file__) + '/test_insert_input_plans_.txt'
        outputfilepath = os.path.dirname(__file__) + '/test_insert_output_plans.txt'
        text_to_add = 'Sunbathing'
        d = 7
        shutil.copy(filepath, newfilepath)
        add_text_in_file(newfilepath, text_to_add, d)
        with open(outputfilepath) as f:
            correct_output = f.read()
        with open(newfilepath) as f:
            output = f.read()
        os.remove(newfilepath)
        assert output == correct_output
        

    def test_update_info(self):
        filepath = os.path.dirname(__file__) + '/test_update_input_plans.txt'
        newfilepath = os.path.dirname(__file__) + '/test_update_input_plans_.txt'
        outputfilepath = os.path.dirname(__file__) + '/test_update_output_plans.txt'
        text_to_add = 'Jogging'
        d = 10
        shutil.copy(filepath, newfilepath)
        add_text_in_file(newfilepath, text_to_add, d)
        with open(outputfilepath) as f:
            correct_output = f.read()
        with open(newfilepath) as f:
            output = f.read()
        os.remove(newfilepath)
        assert output == correct_output
        

    def test_non_existing_file(self):
        filepath = os.path.dirname(__file__) + '/non-existing.txt'
        text_to_add = 'Sunbathing'
        d = 7
        with self.assertRaises(FileNotFoundError):
            add_text_in_file(filepath, text_to_add, d)
