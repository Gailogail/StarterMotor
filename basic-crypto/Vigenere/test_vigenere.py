"""
Tests for encryption and decryption using a Vigenere cipher.
"""
import unittest

from vigenere import vigenere_encrypt
from vigenere import vigenere_decrypt
from vigenere import VigenereCipher


class TestVigenereEncrypt(unittest.TestCase):

    def test_simple_encrypt(self):
        plain_text = "test"
        key = "abcd"
        expected = "TFUW"
        self.assertEqual(vigenere_encrypt(plain_text, key), expected)


class TestVigenereDecrypt(unittest.TestCase):

    def test_simple_decrypt(self):
        cipher_text = "TFUW"
        key = "abcd"
        expected = "test"
        self.assertEqual(vigenere_decrypt(cipher_text, key), expected)


class TestVigenereCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = VigenereCipher("abcd")

    def test_setup_short_key_fails(self):
        key = "a"
        self.assertRaises(ValueError, VigenereCipher, key)

    def test_setup_non_str_key_fails(self):
        key = 1
        self.assertRaises(TypeError, VigenereCipher, key)

    def test_setup_non_alphabetic_character_fails(self):
        key = "abc)"
        self.assertRaises(ValueError, VigenereCipher, key)

    def test_get_key_advances_current_position(self):
        key = self.cipher.get_key()
        self.assertEqual(key, 0)
        self.assertEqual(self.cipher.current, 1)

    def test_get_key_wrap_current_position(self):
        # Key has length 4
        self.cipher.get_key()  # 1
        self.cipher.get_key()  # 2
        self.cipher.get_key()  # 3
        self.cipher.get_key()  # 4 == 0 mod 4
        self.assertEqual(self.cipher.current, 0)
    
    def test_encrypt_basic(self):
        plain_text = "test"
        expected = "TFUW"
        self.assertEqual(self.cipher.encrypt(plain_text), expected)

    def test_decrypt_basic(self):
        cipher_text = "TFUW"
        expected = "test"
        self.assertEqual(self.cipher.decrypt(cipher_text), expected)

    def test_encrypt_char_alphabetical(self):
        char = "a"
        expected = "A"
        self.assertEqual(self.cipher.encrypt_char(char), expected)

    def test_encrypt_char_non_alphabetical(self):
        char = "0"
        expected = "0"
        self.assertEqual(self.cipher.encrypt_char(char), expected)

    def test_decrypt_char_alphabetical(self):
        char = "A"
        expected = "a"
        self.assertEqual(self.cipher.decrypt_char(char), expected)

    def test_decrypt_char_non_alphabetical(self):
        char = "0"
        expected = "0"
        self.assertEqual(self.cipher.decrypt_char(char), expected)

