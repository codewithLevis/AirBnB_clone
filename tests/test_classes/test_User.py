#!/usr/bin/python3
"""
Test User Class
"""
from models.user import User
from tests.test_classes import test_BaseModel
import unittest


class TestUser(test_BaseModel.TestBaseModel):
    """
    instantiate TestUser
    """
    def setUp(self):
        self.my_model = User()
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
    suite.addTests(loader.loadTestsFromTestCase(TestUser))
    runner = unittest.TextTestRunner()
    runner.run(suite)
