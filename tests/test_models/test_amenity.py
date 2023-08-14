from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):

    # Tests that an instance of Amenity can be created with a name attribute
    def test_amenity_instance_creation(self):
        amenity = Amenity()
        amenity.name = 'Pool'
        self.assertEqual(amenity.name, 'Pool')

    # Tests that the name attribute of an Amenity instance can be accessed
    def test_access_name_attribute(self):
        amenity = Amenity()
        amenity.name = 'Pool'
        self.assertEqual(amenity.name, 'Pool')

    # Tests that calling the save method of an Amenity instance
    # updates the updated_at attribute
    def test_save_method_updates_updated_at_attribute(self):
        amenity = Amenity()
        original_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(original_updated_at, amenity.updated_at)

    # Tests that creating an instance of Amenity without a name
    # attribute raises a TypeError
    def test_amenity_without_name_attribute(self):
        with self.assertRaises(TypeError):
            Amenity()

    # Tests that the to_dict method of an Amenity instance returns
    #  a dictionary with the expected attributes
    def test_amenity_to_dict(self):
        amenity = Amenity()
        amenity.name = 'Pool'
        dict_rep = amenity.to_dict()
        self.assertEqual(dict_rep['name'], 'Pool')
        self.assertEqual(dict_rep['__class__'], 'Amenity')
        self.assertTrue('id' in dict_rep)
        self.assertTrue('created_at' in dict_rep)
        self.assertTrue('updated_at' in dict_rep)

    # Tests that an instance of Amenity cannot be created with
    # a non-string name attribute
    def test_non_string_name_attribute(self):
        with self.assertRaises(TypeError):
            Amenity(name=123)

    # Tests that calling the save method of an Amenity instance after
    #  updating the name attribute updates the updated_at attribute
    def test_save_method_updates_updated_at_attribute(self):
        amenity = Amenity()
        amenity.name = 'Test Amenity'
        original_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(original_updated_at, amenity.updated_at)

    # Tests that the to_dict method of an Amenity instance returns a
    #  dictionary with the updated name attribute
    def test_amenity_to_dict_with_updated_name(self):
        amenity = Amenity()
        amenity.name = 'Pool'
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], 'Pool')


if __name__ == '__main__':
    unittest.main()
