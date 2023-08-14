from models.city import City
import unittest


class TestCity(unittest.TestCase):

    # Tests that a City object can be created with state_id and name attributes
    def test_city_creation(self):
        city = City(state_id='CA', name='San Francisco')
        self.assertEqual(city.state_id, 'CA')
        self.assertEqual(city.name, 'San Francisco')

    # Tests that a City object can be converted to a dictionary
    def test_city_to_dict(self):
        city = City()
        city.state_id = 'CA'
        city.name = 'San Francisco'
        city_dict = city.to_dict()
        self.assertEqual(city_dict['state_id'], 'CA')
        self.assertEqual(city_dict['name'], 'San Francisco')
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertTrue('id' in city_dict)
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)

    # Tests that creating a City object with state_id and name attributes
    # that are too long raises a ValueError
    def test_long_attributes(self):
        with self.assertRaises(ValueError):
            City(state_id='a'*65, name='b'*129)

    # Tests that a City object can be created with special characters
    # in its state_id and name attributes
    def test_special_characters_in_attributes(self):
        city = City(state_id='!@#$%^&*()', name='!@#$%^&*()')
        self.assertEqual(city.state_id, '!@#$%^&*()')
        self.assertEqual(city.name, '!@#$%^&*()')

    # Tests that a City object cannot be created with invalid created_at
    # and updated_at attributes
    def test_invalid_created_updated_at(self):
        with self.assertRaises(ValueError):
            City(created_at='invalid', updated_at='invalid')


if __name__ == '__main__':
    unittest.main()
