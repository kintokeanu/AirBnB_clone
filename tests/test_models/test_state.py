from models.state import State
import unittest


class TestState(unittest.TestCase):

    # Tests that a new State object can be created with a name attribute
    def test_state_creation_with_name_attribute(self):
        state = State(name='California')
        self.assertEqual(state.name, 'California')

    # Tests that the State object has id, created_at, and updated_at attributes
    def test_state_has_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))

    # Tests that calling the save method on a State object updates
    #  the updated_at attribute
    def test_save_updates_updated_at_attribute(self):
        state = State()
        old_updated_at = state.updated_at
        state.save()
        new_updated_at = state.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == '__main___':
    unittest.main()
