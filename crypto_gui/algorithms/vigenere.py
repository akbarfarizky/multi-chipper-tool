
import string

ALPHABET_UP = string.ascii_uppercase
ALPHABET_LOW = string.ascii_lowercase

def _key_stream(key: str, n: int):
    cleaned = [c for c in key if c.isalpha()]
    if not cleaned:
        raise ValueError("Kunci Vigenère harus berisi huruf A-Z saja.")
    shifts = [(ord(c.upper()) - ord('A')) % 26 for c in cleaned]
    i = 0
    for _ in range(n):
        yield shifts[i % len(shifts)]
        i += 1

def _vig_char(ch, k):
    if ch.isupper():
        idx = ord(ch) - ord('A')
        return chr(ord('A') + (idx + k) % 26)
    elif ch.islower():
        idx = ord(ch) - ord('a')
        return chr(ord('a') + (idx + k) % 26)
    else:
        return ch

def _vig_char_dec(ch, k):
    return _vig_char(ch, -k)

def encrypt(text: str, key: str) -> str:
    ks = _key_stream(key, len(text))
    out = []
    for ch in text:
        k = next(ks)
        if ch.isalpha():
            out.append(_vig_char(ch, k))
        else:
            out.append(ch)
    return "".join(out)

def decrypt(text: str, key: str) -> str:
    ks = _key_stream(key, len(text))
    out = []
    for ch in text:
        k = next(ks)
        if ch.isalpha():
            out.append(_vig_char_dec(ch, k))
        else:
            out.append(ch)
    return "".join(out)
