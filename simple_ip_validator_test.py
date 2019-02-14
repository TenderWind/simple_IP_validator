# coding: UTF-8


from unittest.case import TestCase

from simple_ip_validator import is_valid_ip


class SimpleIpValidatorTest(TestCase):

    def test_is_valid_ip(self):
        self.assertTrue(is_valid_ip('12.255.56.1'))
        self.assertFalse(is_valid_ip(''))
        self.assertFalse(is_valid_ip('abc.def.ghi.jkl'))
        self.assertFalse(is_valid_ip('123.456.789.0'))
        self.assertFalse(is_valid_ip('12.34.56'))
        self.assertFalse(is_valid_ip('12.34.56 .1'))
        self.assertFalse(is_valid_ip('12.34.56.-1'))
        self.assertFalse(is_valid_ip('123.045.067.089'))
        self.assertTrue(is_valid_ip('127.1.1.0'))
        self.assertTrue(is_valid_ip('0.0.0.0'))
        self.assertTrue(is_valid_ip('0.34.82.53'))
        self.assertFalse(is_valid_ip('192.168.1.300'))
        self.assertFalse(is_valid_ip('192.168.1.2.3'))
        self.assertFalse(is_valid_ip('192.168.1.2.'))
        self.assertFalse(is_valid_ip('192..1.2.'))
        self.assertFalse(is_valid_ip('holy grenade'))
