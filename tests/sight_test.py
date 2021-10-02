import unittest
from models.sight import Sight

class TestSight(unittest.TestCase):

    def setUp(self):
        self.sight1 = Sight("Sydney Opera House", "Sydney", True)
        self.sight2 = Sight("Temple of Literature", "Hanoi", False)


    def test_sight1_has_name(self):
        self.assertEqual("Sydney Opera House", self.sight1.name)

    def test_sight2_has_name(self):
        self.assertEqual("Temple of Literature", self.sight2.name)

    def test_sight1_visited_true(self):
        self.assertEqual(True, self.sight1.visited)

    def test_sight2_visited_false(self):
        self.assertEqual(False, self.sight2.visited)