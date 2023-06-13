import unittest
from app.models import determine_level

class TestModels(unittest.TestCase):
    def test_determine_level(self):
        # Test cases with expected levels
        self.assertEqual(determine_level(10, 0, 0, ['Scratch'], [], 1), 'Beginner')
        self.assertEqual(determine_level(12, 1, 1, ['Python'], ['PyCharm'], 2), 'Intermediate')
        self.assertEqual(determine_level(8, 2, 2, ['JavaScript'], ['Visual Studio Code'], 3), 'Advanced')

        # Test case with invalid age
        with self.assertRaises(ValueError):
            determine_level(0, 1, 1, ['Scratch'], [], 1)

        # Test case with invalid complexity
        with self.assertRaises(ValueError):
            determine_level(10, 1, 1, ['Scratch'], [], 0)
