import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city1 = City("Sydney", "Australia", True)
        self.city2 = City("Hoi Ann", "Vietnam", False)

    
    def test_city1_has_name(self):
        self.assertEqual("Sydney", self.city1.name)

    def test_city2_has_name(self):
        self.assertEqual("Hoi Ann", self.city2.name)

    def test_city1_visited_is_true(self):
        self.assertEqual(True, self.city1.visited)

    def test_city2_visited_is_false(self):
        self.assertEqual(False, self.city2.visited)