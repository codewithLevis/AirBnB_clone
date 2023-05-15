#!/usr/bin/python3
"""
Test BaseModel Class
"""
import unittest
import uuid
import re
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    subdirectory of testcase
    """
    def setUp(self):
        """
        instantiate a new class
        """
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_init(self):
        """
        test if all init instances meet the required format
        """
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(len(self.my_model.id), 36)
        self.assertTrue(type(self.my_model.id) == str)

    def test_str(self):
        """
        test string representation
        """
        string = self.my_model.__str__()
        pattern = r'\[(\w+)\].+?\((.*?)\).+?({[^{}]*\})'
        regex = re.compile(pattern)
        match = regex.search(string)
        match = match.group()
        self.assertEqual(string, match)

    def tearDown(self):
        """
        Delete the instance
        """
        del self.my_model


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestBaseModel))
    runner = unittest.TextTestRunner
    runner.run(suite)
