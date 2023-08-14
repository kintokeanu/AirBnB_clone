from models.review import Review
import unittest


class TestReview(unittest.TestCase):

    # Tests that a Review object can be created with valid place_id,
    # ser_id and text attributes.
    def test_create_review_with_valid_attributes(self):
        review = Review(place_id='123', user_id='456', text='Great place!')
        self.assertEqual(review.place_id, '123')
        self.assertEqual(review.user_id, '456')
        self.assertEqual(review.text, 'Great place!')

    # Tests that calling save() method on a Review object
    # updates the updated_at attribute.
    def test_save_updates_updated_at(self):
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        new_updated_at = review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    # Tests that the to_dict() method of a Review object returns
    #  a dictionary with all attributes and their values.
    def test_review_to_dict(self):
        review = Review()
        review.place_id = '123'
        review.user_id = '456'
        review.text = 'Great place!'
        review_dict = review.to_dict()
        expected_dict = {
            'id': review.id,
            'created_at': review.created_at.isoformat(),
            'updated_at': review.updated_at.isoformat(),
            'place_id': '123',
            'user_id': '456',
            'text': 'Great place!',
            '__class__': 'Review'
        }
        self.assertDictEqual(review_dict, expected_dict)

    # Tests that a Review object can be created with empty
    # place_id, user_id and text attributes.
    def test_empty_review_creation(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    # Tests that a Review object cannot be created with non-string
    # place_id, user_id and text attributes.
    def test_non_string_attributes(self):
        with self.assertRaises(TypeError):
            review = Review(place_id=123, user_id=456, text=789)

    # Tests that a Review object cannot be created with invalid
    # created_at or updated_at attribute values.
    def test_invalid_created_at_or_updated_at(self):
        with self.assertRaises(ValueError):
            Review(created_at='invalid', updated_at='invalid')

    # Tests that a Review object cannot be created with attributes
    #  that exceed their maximum length.
    def test_max_length_attributes(self):
        with self.assertRaises(ValueError):
            review = Review(place_id='a'*129, user_id='b'*129, text='c'*65536)


if __name__ == '__main__':
    unittest.main()
