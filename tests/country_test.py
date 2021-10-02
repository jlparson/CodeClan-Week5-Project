import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country("Australia", True)
        self.country2 = Country("Vietnam", False)


    def test_country1_has_name(self):
        self.assertEqual("Australia", self.country1.name)

    def test_country2_has_name(self):
        self.assertEqual("Vietnam", self.country2.name)

    def test_country1_visited_true(self):
        self.assertEqual(True, self.country1.visited)

    def test_country2_visited_false(self):
        self.assertEqual(False, self.country2.visited)
