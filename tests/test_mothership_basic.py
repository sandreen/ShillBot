
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
    def test_mothership_creation(self):
        mother = MothershipServer()

        self.assertIsInstance(mother, MothershipServer)

    def test_mothership_timeout(self):
        mother = None
        mother = MothershipServer()

        self.assertRaises(timeout, mother.run)
