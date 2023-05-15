#!/usr/bin/python3
"""
test the Json storage
"""
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
import unittest
import os
import datetime


class TestFileStorage(unittest.TestCase):
    """
    subclass unittest.TestCase
    """
    def setUp(self):
        self.new = City()

    def test_file_json(self):
        self.new.save()
        file_name = "file.json"
        exists = os.path.exists(file_name)
        self.assertTrue(exists)
        self.assertIsNotNone(storage._FileStorage__file_path)

    def test_obj(self):
        self.assertIs(type(storage._FileStorage__objects), dict)

    def test_all(self):
        new_d = storage.all()
        self.assertGreater(len(new_d), 0)

    def test_new(self):
        new_model = City()
        new_d = storage.all()
        search_key = f'{new_model.__class__.__name__}.{new_model.id}'
        self.assertIn(search_key, new_d)
        del storage._FileStorage__objects[search_key]

    def test_save(self):
        new_model = City()
        search_key = f'{new_model.__class__.__name__}.{new_model.id}'
        storage.save()
        with open('file.json', encoding='utf-8') as file:
            data = file.read()
            self.assertIn(search_key, data)
        del storage._FileStorage__objects[search_key]
        storage.save()
        with open('file.json', encoding='utf-8') as file:
            data = file.read()
            self.assertNotIn(search_key, data)

    def test_reload(self):
        new_model = City()
        search_key = f'{new_model.__class__.__name__}.{new_model.id}'
        storage.save()
        all_s = storage.all()
        storage.reload()
        self.assertEqual(all_s, storage._FileStorage__objects)
        obj = storage._FileStorage__objects[search_key]
        self.assertIsNot(type(obj.created_at), str)
        self.assertIs(type(obj.created_at), datetime.datetime)
        del storage._FileStorage__objects[search_key]

    def tearDown(self):
        search_key = f'{self.new.__class__.__name__}.{self.new.id}'
        del storage._FileStorage__objects[search_key]


if __name__ == '__main__':
    unittest.main()
