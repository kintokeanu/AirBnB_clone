from models.user import User
import unittest


class TestUser(unittest.TestCase):

    # Tests that a new user can be created with valid email,
    # password, first_name, and last_name
    def test_create_new_user_with_valid_details(self):
        user = User(email='test@test.com', password='password',
                    first_name='Test', last_name='User')
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')

    # Tests that the User object has the correct email, password,
    #  first_name, and last_name attributes
    def test_user_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    # Tests that the email, password, first_name, and last_name
    # attributes of the User object can be updated
    def test_update_user_attributes(self):
        user = User()
        user.email = 'test@test.com'
        user.password = 'password'
        user.first_name = 'John'
        user.last_name = 'Doe'
        self.assertEqual(user.email, 'test@test.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    # Tests that calling the save() method on a User object
    #  updates the updated_at attribute
    def test_save_updates_updated_at(self):
        user = User()
        old_updated_at = user.updated_at
        user.save()
        new_updated_at = user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    # Tests that the to_dict() method on the User object returns a
    # dictionary with all attributes set correctly
    def test_user_to_dict(self):
        user = User(email='test@test.com', password='password',
                    first_name='John', last_name='Doe')
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'test@test.com')
        self.assertEqual(user_dict['password'], 'password')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    # Tests that creating a new User object with an empty email
    #  string raises a ValueError
    def test_empty_email(self):
        with self.assertRaises(ValueError):
            User(email='')

    # Tests that a User object can be created with an empty
    # last_name string
    def test_empty_last_name(self):
        user = User(last_name='')
        self.assertIsInstance(user, User)
        self.assertEqual(user.last_name, '')

    # Tests that creating a new User object with an invalid email string
    # format raises a ValueError.
    def test_invalid_email_format(self):
        with self.assertRaises(ValueError):
            User(email='invalid_email_format', password='password',
                 first_name='John', last_name='Doe')


if __name__ == '__main__':
    unittest.main()
