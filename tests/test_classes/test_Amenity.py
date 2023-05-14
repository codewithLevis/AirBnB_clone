#!/usr/bin/python3
"""
Test Amenity Class
"""
from models.amenity import Amenity
from tests.test_classes import test_BaseModel
import unittest


class TestAmenity(test_BaseModel.TestBaseModel):
    """
    instantiate TestBaseModel
    """
    def setUp(self):
        self.my_model = Amenity()
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
    suite.addTests(loader.loadTestsFromTestCase(TestAmenity))
    runner = unittest.TextTestRunner()
    runner.run(suite)
