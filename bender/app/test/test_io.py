""" Test module for mt I/O """
import unittest
from app.controllers.mt_io import print_err, print_info


class MTIOUnitTest(unittest.TestCase):
    """ Test case for I/O """
    def test_io_err(self):
        """ test printing error message, expect True """
        response = print_err('here is an error.')
        assert response is True

    def test_io_info(self):
        """ test printing info message, expect True """
        response = print_info('here is a message.')
        assert response is True
