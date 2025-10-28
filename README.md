
# Classic Ciphers GUI (Caesar • Vigenère • Hill • Transposition • ROT13)

Aplikasi GUI sederhana untuk enkripsi & dekripsi menggunakan algoritma klasik:
- **Caesar**
- **Vigenère**
- **Hill (2x2)**
- **Columnar Transposition**
- **ROT13** (tanpa kunci)

Dibuat dengan **Python + Tkinter**. Mendukung **import** teks dari file `.txt` dan **export** hasil output ke `.txt`.

## Struktur Proyek

```
crypto_classic_gui/
├─ main.py
├─ crypto_gui/
│  ├─ __init__.py
│  ├─ app.py                # GUI (Tkinter)
│  ├─ algorithms/
│  │  ├─ __init__.py
│  │  ├─ caesar.py
│  │  ├─ vigenere.py
│  │  ├─ hill.py            # Hill 2x2
│  │  ├─ transposition.py   # Columnar Transposition
│  │  └─ rot13.py
│  └─ utils/
│     ├─ __init__.py
│     ├─ file_io.py
│     └─ text_utils.py
└─ requirements.txt
```

## Cara Menjalankan (Visual Studio Code)

1. Pastikan **Python 3.9+** terpasang. (Tkinter biasanya sudah ada secara default.)
2. Buka folder proyek `crypto_classic_gui` di **Visual Studio Code**.
3. (Opsional) Buat virtual environment, lalu:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan:
   ```bash
   python main.py
   ```

## Penggunaan

- **Toolbar/Menu**:
  - **Algoritma**: pilih Caesar, Vigenère, Hill (2x2), Transposition, atau ROT13.
  - **Mode**: Encrypt / Decrypt.
  - **Kunci**:
    - *Caesar*: angka (mis. `3`).
    - *Vigenère*: kata/huruf saja (mis. `RAHASIA`). Karakter non-huruf diabaikan.
    - *Hill (2x2)*: 4 angka (mis. `3 3 2 5`) **atau** 4 huruf (mis. `HILL`). 
      - **Catatan**: kunci harus memiliki determinan yang relatif prima terhadap 26 agar dapat diinvers.
      - Plaintext diproses **huruf A–Z** saja; karakter lain dibuang. Bila ganjil, akan dipadding `X`.
    - *Transposition*: kata kunci huruf (mis. `KUNCI`). Plaintext akan dibersihkan ke huruf A–Z (spasi/tanda baca dihapus) sesuai praktik klasik.
    - *ROT13*: tidak butuh kunci.
  - **Import .txt**: memuat file teks ke area input.
  - **Export Output**: menyimpan area output (hasil) ke `.txt`.
- **Area Input**: masukkan **plaintext** (untuk Encrypt) atau **ciphertext** (untuk Decrypt).
- Tekan **Proses** untuk menjalankan, hasil tampil di **Output**.

## Catatan & Batasan

- Implementasi ditujukan untuk pembelajaran kriptografi klasik:
  - **Caesar/Vigenère/ROT13**: mempertahankan huruf besar-kecil dan membiarkan non-huruf apa adanya.
  - **Hill (2x2)**: hanya huruf A–Z, uppercase; non-huruf dibuang. Panjang ganjil → padding `X`. 
  - **Transposition**: huruf A–Z saja (uppercase), non-huruf dihapus, padding `X` jika diperlukan.
- Dekripsi **Hill** membutuhkan kunci yang **valid** (determinannya invertible modulo 26). Jika tidak, aplikasi akan menampilkan pesan error.

## Lisensi

MIT — bebas digunakan untuk keperluan pembelajaran.
