from unittest import TestCase

import py_out
import sys

class TestPrime(TestCase):

  def setUp(self):
    """Init"""

  def test_get_site_package(self):
    """Test for get_site_package"""
    self.assertFalse(py_out.get_site_package(4))
    self.assertTrue(py_out.get_site_package(10))


  def tearDown(self):
    """Finish"""