"""
Encrypt and decrypt text using a Vigenere cipher.

The Vigenere cipher is a variant on the Ceasar cipher, which encypts each
character using a shift, but the shift value changes over the text according
to a predefined key, which is usually a codeword. For example, using the key
"cow", which corresponds to shifts of 2, 14, and 22. 

Example:
>>> plain_text = "I am writing Python code, yay!"
>>> key = "parrot"
>>> cipher_text = vigenere_encrypt(plain_text, key)
>>> cipher_text
'X AD NFBIIEX DRIHFE QHSE, PRM!'
>>> vigenere_decrypt(cipher_text, key)
'i am writing python code, yay!'
"""
import string

class VigenereCipher:
    """
    Object representing a Vigenere cipher.

    This object holds the state of the cipher, so that the shift
    can be chosen correctly each time a new (text) character, is
    encrypted or decrypted. It is not easy to maintain this state
    without using a class.

    A key must be provided when instantiating a cipher object. Once created,
    the cipher can be used to encrypt or decrypt text using the `encrypt` or
    `decrypt` methods.

    The actual encryption and decryption happens in the `encrypt_char` and
    `decrypt_char` methods, which filter out non-alphabetic characters before
    encrypting.
    """
    
    def __init__(self, key):
        # Be a good Python citizen, check your inputs!
        if not isinstance(key, str):
            raise TypeError("Key must be a string")

        if not len(key) >= 2:
            raise ValueError("Key must have at least two characters")

        key = key.lower()
        # Since we ignore non-alphabetic characters, we should make sure
        # our key doesn't contain any such characters.
        if not all(c in string.ascii_lowercase for c in key):
            raise ValueError("Key must contain only alphabetic characters")

        self.key = [ord(c) - 97 for c in key]
        self.current = 0
   
    def get_key(self):
        key = self.key[self.current]
        self.current = (self.current + 1) % len(self.key)
        return key

    def encrypt_char(self, character):   
        """
        Encode a character using the cipher.
        """
        char_index = ord(character)
        if not 97 <= char_index <= 122:
            return character
        char_index -= 97
        return chr((char_index + self.get_key()) % 26 + 65)
        
    def encrypt(self, text):
        """
        Encrypt a string using the cipher.
        """
        return "".join(self.encrypt_char(c) for c in text.lower())

    def decrypt_char(self, character):
        """
        Decrypt a character using the cipher.
        """
        char_index = ord(character)
        if not 65 <= char_index <= 90:
            return character
        char_index -= 65
        return chr((char_index - self.get_key()) % 26 + 97)

    def decrypt(self, text):
        """
        Decrypt text using the cipher.
        """
        return "".join(self.decrypt_char(c) for c in text.upper())


def vigenere_encrypt(text, key):
    """
    Encrypt text using a Vigenere cipher.

    Example:
    >>> plain_text = "attackatdawn"
    >>> key = "lemon"
    >>> vigenere_encrypt(plain_text, key)
    'LXFOPVEFRNHR'
    """
    cipher = VigenereCipher(key)
    return cipher.encrypt(text)


def vigenere_decrypt(text, key):
    """
    Decrypt text using a Vigenere cipher.

    Example:
    >>> cipher_text = "LXFOPVEFRNHR"
    >>> key = "lemon"
    >>> vigenere_decrypt(cipher_text, key)
    'attackatdawn'
    """
    cipher = VigenereCipher(key)
    return cipher.decrypt(text)
