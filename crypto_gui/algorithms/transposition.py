
import math

def _rank_key(keyword: str):
    # rank letters by alphabetical order; stable on equal letters
    cleaned = [c for c in keyword if c.isalpha()]
    if not cleaned:
        raise ValueError("Kata kunci Transposition harus berisi huruf (A-Z).")
    # store original positions
    pairs = list(enumerate([c.lower() for c in cleaned]))
    # sort by character then by original index to make it stable
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
    # build rank mapping: col index -> order number
    rank = [0]*len(cleaned)
    for order, (orig_idx, _) in enumerate(sorted_pairs):
        rank[orig_idx] = order
    return rank

def _clean(text: str):
    # For classic columnar transposition, remove non-letters and uppercase
    return "".join([c for c in text.upper() if c.isalpha()])

def encrypt(text: str, keyword: str) -> str:
    rank = _rank_key(keyword)
    clean = _clean(text)
    cols = len(rank)
    rows = math.ceil(len(clean) / cols) if cols > 0 else 0
    # pad with X
    padded = clean.ljust(rows*cols, 'X')
    # fill matrix row-wise
    matrix = [list(padded[r*cols:(r+1)*cols]) for r in range(rows)]
    # read columns by increasing rank
    ciphertext = []
    for order in range(cols):
        col_idx = rank.index(order)
        for r in range(rows):
            ciphertext.append(matrix[r][col_idx])
    return "".join(ciphertext)

def decrypt(text: str, keyword: str) -> str:
    rank = _rank_key(keyword)
    cols = len(rank)
    clean = "".join([c for c in text.upper() if c.isalpha()])
    n = len(clean)
    if cols == 0:
        return ""
    rows = math.ceil(n / cols)
    # number of full cells
    full_cells = n
    # determine column lengths (all equal because padded in encryption, but handle general case)
    base_len = n // cols
    extra = n % cols
    col_lengths = [base_len] * cols
    # The first 'extra' columns in rank order get +1
    for order in range(extra):
        col_idx = rank.index(order)
        col_lengths[col_idx] += 1

    # read columns into list by rank order
    cols_data = [''] * cols
    idx = 0
    for order in range(cols):
        col_idx = rank.index(order)
        L = col_lengths[col_idx]
        cols_data[col_idx] = clean[idx:idx+L]
        idx += L

    # reconstruct row-wise
    plaintext = []
    for r in range(rows):
        for c in range(cols):
            if r < len(cols_data[c]):
                plaintext.append(cols_data[c][r])
    return "".join(plaintext).rstrip('X')
