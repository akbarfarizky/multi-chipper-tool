
import string

def _rot13_char(ch):
    if 'A' <= ch <= 'Z':
        return chr((ord(ch) - ord('A') + 13) % 26 + ord('A'))
    if 'a' <= ch <= 'z':
        return chr((ord(ch) - ord('a') + 13) % 26 + ord('a'))
    return ch

def encrypt(text: str, key: str = "") -> str:
    # key is ignored
    return "".join(_rot13_char(c) for c in text)

def decrypt(text: str, key: str = "") -> str:
    # ROT13 is involutory
    return "".join(_rot13_char(c) for c in text)
