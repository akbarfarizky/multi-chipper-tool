
import string

ALPHABET_UP = string.ascii_uppercase
ALPHABET_LOW = string.ascii_lowercase

def _shift_char(ch, k):
    if ch.isupper():
        idx = ALPHABET_UP.find(ch)
        if idx == -1:
            return ch
        return ALPHABET_UP[(idx + k) % 26]
    elif ch.islower():
        idx = ALPHABET_LOW.find(ch)
        if idx == -1:
            return ch
        return ALPHABET_LOW[(idx + k) % 26]
    else:
        return ch

def encrypt(text: str, key: int) -> str:
    try:
        k = int(key)
    except Exception:
        raise ValueError("Kunci Caesar harus berupa angka (contoh: 3).")
    return "".join(_shift_char(c, k) for c in text)

def decrypt(text: str, key: int) -> str:
    try:
        k = int(key)
    except Exception:
        raise ValueError("Kunci Caesar harus berupa angka (contoh: 3).")
    return "".join(_shift_char(c, -k) for c in text)
