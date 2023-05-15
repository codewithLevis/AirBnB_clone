#!/usr/bin/python3
"""
test the Json storage
"""
from models.engine.file_storage import FileStorage
from models import storage
from models.city import BaseModel
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """
    subclass unittest.TestCase
    """
    def setUp(self):
        pass

    def test_file_json(self):
        self.new = BaseModel()
        self.new.save()
        file_name = "file.json"
        exists = os.path.exists(file_name)
        self.assertTrue(exists)

    def test_reload(self):
        storage.reload()
        self.assertIsNotNone(storage)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
