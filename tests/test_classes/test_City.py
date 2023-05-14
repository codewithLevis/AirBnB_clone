#!/usr/bin/python3
"""
Test City Class
"""
from models.city import City
from tests.test_classes import test_BaseModel
import unittest


class TestCity(test_BaseModel.TestBaseModel):
    """
    instantiate TestCity
    """
    def setUp(self):
        self.my_model = City()
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
    suite.addTests(loader.loadTestsFromTestCase(TestCity))
    runner = unittest.TextTestRunner
    runner.run(suite)
