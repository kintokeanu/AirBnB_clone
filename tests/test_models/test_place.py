from models.place import Place
from datetime import datetime
import unittest


class TestPlace(unittest.TestCase):

    # Tests that the save() method updates the updated_at attribute of
    # the object with the current datetime.
    def test_save_method(self):
        place = Place()
        old_updated_at = place.updated_at
        place.save()
        new_updated_at = place.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    # Test that the __str__() method returns the correct string
    #  representation of the object.
    def test_str_method_returns_correct_string_representation(self):
        place = Place()
        expected_output = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_output)

    # Tests that an instance of Place cannot be created with
    # invalid attribute types
    def test_invalid_attribute_types(self):
        with self.assertRaises(TypeError):
            Place(city_id=1, user_id=2, name=3, description=4,
                  number_rooms='5',
                  number_bathrooms='6', max_guest='7', price_by_night='8',
                  latitude='9', longitude='10', amenity_ids='11')

    # Tests that an instance of Place can be created with all attributes
    def test_create_place_with_all_attributes(self):
        place = Place(city_id='1', user_id='2', name='test',
                      description='test',
                      number_rooms=1, number_bathrooms=1, max_guest=1,
                      price_by_night=1,
                      latitude=1.0, longitude=1.0, amenity_ids=['1', '2'])
        self.assertEqual(place.city_id, '1')
        self.assertEqual(place.user_id, '2')
        self.assertEqual(place.name, 'test')
        self.assertEqual(place.description, 'test')
        self.assertEqual(place.number_rooms, 1)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 1)
        self.assertEqual(place.price_by_night, 1)
        self.assertEqual(place.latitude, 1.0)
        self.assertEqual(place.longitude, 1.0)
        self.assertEqual(place.amenity_ids, ['1', '2'])

    # Tests that the to_dict() method returns a dictionary with the
    # correct attributes
    def test_to_dict_method(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['city_id'], '')
        self.assertEqual(place_dict['user_id'], '')
        self.assertEqual(place_dict['name'], '')
        self.assertEqual(place_dict['description'], '')
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])

    # Tests that setting attributes of an instance of Place and calling save()
    #  method updates the updated_at attribute of the object with the current
    #  datetime.
    def test_set_attributes_and_save(self):
        place = Place()
        place.city_id = '123'
        place.user_id = '456'
        place.name = 'Test Place'
        place.description = 'A test place'
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ['1', '2', '3']
        old_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(old_updated_at, place.updated_at)

    # Tests that calling save() method on an instance of Place with no
    #  updated_at attribute sets the updated_at attribute to the current
    # datetime.
    def test_save_with_no_updated_at_attribute(self):
        place = Place()
        self.assertFalse(hasattr(place, 'updated_at'))
        place.save()
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertIsInstance(place.updated_at, datetime)

    # Tests that to_dict() method returns a dictionary with all attributes,
    # including __class__, created_at and updated_at, and that created_at
    # and updated_at are datetime objects
    def test_to_dict_no_created_at(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)
        self.assertIsInstance(datetime.strptime(place_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime)
        self.assertIsInstance(datetime.strptime(place_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'), datetime)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], '')
        self.assertEqual(place_dict['user_id'], '')
        self.assertEqual(place_dict['name'], '')
        self.assertEqual(place_dict['description'], '')
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])

    # Tests that to_dict() method returns a dictionary with the correct
    # attributes when called on an instance of Place with no
    #  updated_at attribute
    def test_to_dict_no_updated_at(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], place.id)
        self.assertEqual(place_dict['created_at'],
                         place.created_at.isoformat())
        self.assertNotIn('updated_at', place_dict)
        self.assertEqual(place_dict['city_id'], '')
        self.assertEqual(place_dict['user_id'], '')
        self.assertEqual(place_dict['name'], '')
        self.assertEqual(place_dict['description'], '')
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guest'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])


if __name__ == '__main__':
    unittest.main()
