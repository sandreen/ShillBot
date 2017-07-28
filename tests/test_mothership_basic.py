
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):

    def test_mothershit_initialization(self):
        mother = MothershipServer()
        motherPort = mother.port

        self.assertEqual(motherPort, 8080)
