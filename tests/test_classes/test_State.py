#!/usr/bin/python3
"""
Test State Class
"""
from models.state import State
from tests.test_classes import test_BaseModel
import unittest


class TestState(test_BaseModel.TestBaseModel):
    """
    instantiate TestState
    """
    def setUp(self):
        self.my_model = State()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_init(self):
        return super().test_init()

    def test_str(self):
        return super().test_str()

    def tearDown(self):
        return super().tearDown()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestState))
    runner = unittest.TextTestRunner()
    runner.run(suite)
