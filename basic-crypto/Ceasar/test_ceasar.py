"""
Tests for the Ceaser cipher encryption and decryption.
"""
import unittest

from ceasar import ceasar_encrypt
from ceasar import ceasar_decrypt


class TestCeasarEncrypt(unittest.TestCase):

    def test_simple_encrypt(self):
        plain_text = "test"
        key = 1
        expected = "UFTU"
        self.assertEqual(ceasar_encrypt(plain_text, key), expected)

    def test_bad_key_throws_exception(self):
        plain_text = "test"
        key = 0
        self.assertRaises(ValueError, ceasar_encrypt, plain_text, key) 

class TestCeasarDecrypt(unittest.TestCase):

    def test_simple_decrypt(self):
        cipher_text = "UFTU"
        key = 1
        expected = "test"
        self.assertEqual(ceasar_decrypt(cipher_text, key), expected)

    def test_bad_key_throws_exception(self):
        plain_text = "UFTU"
        key = 0
        self.assertRaises(ValueError, ceasar_decrypt, plain_text, key) 
