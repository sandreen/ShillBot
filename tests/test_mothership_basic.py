
import unittest
import socket
import os

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
    def test_mothership_creation(self):
        mother = MothershipServer()

        self.assertIsInstance(mother, MothershipServer)
