import unittest
from flipexception import FlipException, ValueError


class FlipAllTheThings(unittest.TestCase):
    def setUp(self):
        pass

    def test_exception_base(self):
        """
        Testing Eexception Base
        """

        with self.assertRaises(Exception):
            raise FlipException()

    def test_exception_flip(self):
        """
        Testing Eexception Base
        """

        with self.assertRaises(FlipException):
            raise FlipException()

    def test_valueerror(self):
        """
        Testing ValueError
        """
        with self.assertRaises(ValueError):
            raise ValueError

