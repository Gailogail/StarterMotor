"""
Encrypt and decrypt text using a Ceasar shift cipher.

The Ceasar cipher is a simple cryptographic algorithm that takes plain text
and simply shifts to the character a given number of places to the right to
create the cipher text. For example, using a shift of 5, the letter a would
be encoded as F, the letter b as G, and so on.

This module contains two functions: ceasar_encrypt and ceasar_decrypt.
Both take two arguments, the text to encrypt or decrypt and the cipher key.
For simplicity, we only modify alphabetical characters, and leave numbers, 
punctuation, and spaces unchanged.

Example:
>>> plain_text = "this is some text"
>>> key = 5
>>> cipher_text = ceasar_encrypt(plain_text, key)
>>> cipher_text
'YMNX NX XTRJ YJCY'
>>> ceasar_decrypt(cipher_text, key)
'this is some text'
"""


def ceasar_encrypt(text, n):
    """
    Encrypt text using a Ceasar shift of n places.
    
    Spaces and punctuation are preserved. First normalises 
    by converting to lower-case, then applies the shift and
    returns the resulting cipher-text.

    Example:
    >>> plain = "This is a test."
    >>> ceasar_encrypt(plain, 5)
    'YMNX NX F YJXY.'

    Args:
        text - The plain text to encrypt. (str)
        n    - The key (shift) to use (int).

    Returns:
        str  - cipher text
    """
    # Check that the shift amount is valid
    n = n % 26
    if n == 0:
        raise ValueError("A shift of zero performs no encryption")

    text = text.lower()

    # Now we need to create a lookup table to use during encryption
    # We are working with ascii encoded characters (basic text characters)
    # so we need to make sure we get the right numbers to correspond to 
    # upper-case and lower-case characters.
    # The lower-case characters a-z start at 65, and the upper-case
    # characters start at 97.
    # Lower-case characters for plain-text.
    codebook = {}
    for i in range(26):
        # the chr function converts an int to the corresponding character.
        codebook[chr(i + 97)] = chr((i + n) % 26 + 65)
    return "".join(codebook.get(c, c) for c in text)


def ceasar_decrypt(text, n):
    """
    Decode the cipher text using the Ceaser cipher.

    Spaces and punctuation are preserved. First normalises 
    by converting to upper-case, then applies the shift and
    returns the resulting plain text.

    Example:
    >>> plain = "YMNX NX F YJXY."
    >>> ceasar_encrypt(plain, 5)
    'This is a test.'

      
    Args:
        text - The cipher text to decrypt. (str)
        n    - The key (shift) to use (int).

    Returns:
        str  - plain text
    """
    # Check that the shift is valid
    n = n % 26 
    if n == 0:
        raise ValueError("A shift of zero performs no encryption")

    text = text.upper()

    # Create the codebook, upper-case characters represent cipher-text, so
    # we use these as the indices for this codebook.
    codebook = {}
    for i in range(26):
        # the chr function converts an int to the corresponding character.
        codebook[chr(i + 65)] = chr((i - n) % 26 + 97)
    return "".join(codebook.get(c, c) for c in text)



if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("Type the text to encrypt\nCtrl-C to finish")
        lines = []
        while True:
            try:
                c = input("> ")
                lines.append(shift(c, 13))
            except KeyboardInterrupt:
                print('', *lines, sep="\n")
                break
    else:
        print(shift(sys.argv[1], 13))

