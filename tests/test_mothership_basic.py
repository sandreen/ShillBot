
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):

    def test_worker_connection(self):
        mother = None
        mother = MothershipServer()

        self.assertRaises(ValueError, mother.run())
