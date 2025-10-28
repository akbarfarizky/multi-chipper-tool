
import math

def _clean_letters(text: str):
    return "".join([c for c in text.upper() if c.isalpha()])

def _egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = _egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def _modinv(a, m):
    a = a % m
    g, x, y = _egcd(a, m)
    if g != 1:
        raise ValueError("Determinannya tidak invertible modulo 26. Pilih kunci lain.")
    return x % m

def _parse_key_2x2(key: str):
    # Accept "a b c d" (integers) or 4 letters
    parts = key.replace(',', ' ').split()
    if len(parts) == 4 and all(p.lstrip('-').isdigit() for p in parts):
        a, b, c, d = [int(p) % 26 for p in parts]
    else:
        letters = [c for c in key.upper() if c.isalpha()]
        if len(letters) != 4:
            raise ValueError("Kunci Hill 2x2 harus 4 angka (mis. '3 3 2 5') atau 4 huruf (mis. 'HILL').")
        nums = [ord(c) - ord('A') for c in letters]
        a, b, c, d = nums
    det = (a*d - b*c) % 26
    if math.gcd(det, 26) != 1:
        raise ValueError("Determinannya tidak relativ prima terhadap 26. Gunakan kunci lain.")
    return (a, b, c, d), det

def _mat_mult_vec_2x2(mat, vec):
    a, b, c, d = mat
    x, y = vec
    return ((a*x + b*y) % 26, (c*x + d*y) % 26)

def _mat_inv_2x2(mat):
    a, b, c, d = mat
    det = (a*d - b*c) % 26
    inv_det = _modinv(det, 26)
    # inverse matrix: (d, -b, -c, a) * inv_det (mod 26)
    return (
        ( d * inv_det) % 26,
        ((-b) * inv_det) % 26,
        ((-c) * inv_det) % 26,
        ( a * inv_det) % 26
    )

def encrypt(text: str, key: str) -> str:
    mat, _ = _parse_key_2x2(key)
    clean = _clean_letters(text)
    if len(clean) % 2 == 1:
        clean += 'X'
    out = []
    for i in range(0, len(clean), 2):
        x = ord(clean[i]) - ord('A')
        y = ord(clean[i+1]) - ord('A')
        u, v = _mat_mult_vec_2x2(mat, (x, y))
        out.append(chr(u + ord('A')))
        out.append(chr(v + ord('A')))
    return "".join(out)

def decrypt(text: str, key: str) -> str:
    mat, _ = _parse_key_2x2(key)
    inv = _mat_inv_2x2(mat)
    clean = _clean_letters(text)
    if len(clean) % 2 == 1:
        clean += 'X'
    out = []
    for i in range(0, len(clean), 2):
        x = ord(clean[i]) - ord('A')
        y = ord(clean[i+1]) - ord('A')
        u, v = _mat_mult_vec_2x2(inv, (x, y))
        out.append(chr(u + ord('A')))
        out.append(chr(v + ord('A')))
    return "".join(out).rstrip('X')
