from models.engine.file_storage import FileStorage
import unittest
import os


class TestFileStorage(unittest.TestCase):

    # Test that the all() method of FileStorage class returns an
    # empty dictionary when no objects have been added
    def test_all_returns_empty_dict_when_no_objects_added(self):
        fs = FileStorage()
        self.assertEqual(fs.all(), {})

    # Tests that the new() method adds an object to the __objects dictionary
    def test_new_method_adds_object_to_objects_dictionary(self):
        fs = FileStorage()
        obj = {'id': 1, 'name': 'test'}
        fs.new(obj)
        self.assertEqual(fs.all(), {'FileStorage.1': obj})

    # Tests that the all() method returns a dictionary of objects when
    #  objects have been added
    def test_all_returns_dict_of_objects_when_objects_added(self):
        fs = FileStorage()
        obj1 = {'id': 1, 'name': 'test1'}
        obj2 = {'id': 2, 'name': 'test2'}
        fs.new(obj1)
        fs.new(obj2)
        self.assertEqual(fs.all(), {'FileStorage.1': obj1,
                                    'FileStorage.2': obj2})

    # Tests that the new() method sets in __objects the given obj with
    # key <obj class name>.id
    def test_new_method_sets_obj_in_objects_with_key_obj_class_name_id(self):
        fs = FileStorage()
        obj = {'id': 1, 'name': 'test'}
        fs.new(obj)
        self.assertEqual(fs.all(), {'FileStorage.1': obj})

    # Tests that the reload() method does not raise an error when the
    #  JSON file does not exist
    def test_reload_doesnt_raise_error_when_JSON_file_doesnt_exist(self):
        fs = FileStorage()
        fs.reload()
        # No assertion needed, just checking that no error is raised

    # Tests that the save() method creates a new JSON file if it does not exist
    def test_save_method_creates_new_JSON_file_if_it_does_not_exist(self):
        fs = FileStorage()
        fs.save()
        self.assertTrue(os.path.exists(fs._FileStorage__file_path))


if __name__ == '__main__':
    unittest.main()
