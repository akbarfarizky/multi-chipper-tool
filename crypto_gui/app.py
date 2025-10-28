
import tkinter as tk
from tkinter import ttk, messagebox
from .algorithms import caesar, vigenere, hill, transposition, rot13
from .utils import file_io

ALGORITHMS = ["Caesar", "Vigenère", "Hill (2x2)", "Transposition", "ROT13"]

class CryptoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Classic Ciphers GUI — Caesar • Vigenère • Hill • Transposition • ROT13")
        self.root.geometry("980x640")

        self.selected_algo = tk.StringVar(value=ALGORITHMS[0])
        self.mode = tk.StringVar(value="encrypt")  # "encrypt" or "decrypt"
        self.key_var = tk.StringVar(value="3") # default for Caesar
        self.status_var = tk.StringVar(value="Siap.")

        self._build_menu()
        self._build_toolbar()
        self._build_body()
        self._bind_events()

    def _build_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Import .txt → Input", command=lambda: file_io.import_text_to(self.input_txt))
        file_menu.add_command(label="Export Output → .txt", command=lambda: file_io.export_text_from(self.output_txt))
        file_menu.add_separator()
        file_menu.add_command(label="Keluar", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        algo_menu = tk.Menu(menubar, tearoff=0)
        for name in ALGORITHMS:
            algo_menu.add_radiobutton(label=name, variable=self.selected_algo, value=name, command=self._on_algo_change)
        menubar.add_cascade(label="Algoritma", menu=algo_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Tentang", command=self._about)
        menubar.add_cascade(label="Bantuan", menu=help_menu)

        self.root.config(menu=menubar)

    def _build_toolbar(self):
        bar = ttk.Frame(self.root, padding=8)
        bar.pack(side="top", fill="x")

        ttk.Label(bar, text="Algoritma:").pack(side="left")
        self.algo_cb = ttk.Combobox(bar, values=ALGORITHMS, textvariable=self.selected_algo, state="readonly", width=18)
        self.algo_cb.pack(side="left", padx=(6, 12))

        ttk.Label(bar, text="Mode:").pack(side="left", padx=(0,6))
        ttk.Radiobutton(bar, text="Encrypt", variable=self.mode, value="encrypt").pack(side="left")
        ttk.Radiobutton(bar, text="Decrypt", variable=self.mode, value="decrypt").pack(side="left", padx=(0,12))

        self.key_label = ttk.Label(bar, text="Kunci:")
        self.key_label.pack(side="left")
        self.key_entry = ttk.Entry(bar, textvariable=self.key_var, width=28)
        self.key_entry.pack(side="left", padx=(6, 12))

        ttk.Button(bar, text="Proses", command=self._process).pack(side="left")
        ttk.Button(bar, text="Bersihkan", command=self._clear).pack(side="left", padx=(6,0))

        ttk.Button(bar, text="Import", command=lambda: file_io.import_text_to(self.input_txt)).pack(side="right")
        ttk.Button(bar, text="Export", command=lambda: file_io.export_text_from(self.output_txt)).pack(side="right", padx=(0,6))

    def _build_body(self):
        body = ttk.Frame(self.root, padding=8)
        body.pack(fill="both", expand=True)

        # Input
        left = ttk.Frame(body)
        left.pack(side="left", fill="both", expand=True, padx=(0,4))

        ttk.Label(left, text="Input (Plaintext / Ciphertext):").pack(anchor="w")
        self.input_txt = tk.Text(left, wrap="word", height=18)
        self.input_txt.pack(fill="both", expand=True)

        # Output
        right = ttk.Frame(body)
        right.pack(side="left", fill="both", expand=True, padx=(4,0))

        ttk.Label(right, text="Output:").pack(anchor="w")
        self.output_txt = tk.Text(right, wrap="word", height=18, state="normal")
        self.output_txt.pack(fill="both", expand=True)

        # Status bar
        status = ttk.Frame(self.root, padding=4)
        status.pack(side="bottom", fill="x")
        self.status_label = ttk.Label(status, textvariable=self.status_var, anchor="w")
        self.status_label.pack(side="left")

        self._on_algo_change()  # set proper key placeholder

    def _bind_events(self):
        self.algo_cb.bind("<<ComboboxSelected>>", lambda e: self._on_algo_change())

    def _about(self):
        messagebox.showinfo(
            "Tentang",
            "Classic Ciphers GUI\n\nMendukung: Caesar, Vigenère, Hill (2x2), Columnar Transposition, dan ROT13.\n"
            "Dibuat untuk pembelajaran kriptografi klasik."
        )

    def _on_algo_change(self):
        algo = self.selected_algo.get()
        if algo == "Caesar":
            self.key_label.config(text="Kunci (angka):")
            if not self.key_var.get():
                self.key_var.set("3")
            self.key_entry.config(state="normal")
        elif algo == "Vigenère":
            self.key_label.config(text="Kunci (kata):")
            self.key_entry.config(state="normal")
        elif algo == "Hill (2x2)":
            self.key_label.config(text="Kunci 2x2 (4 angka/huruf):")
            if not self.key_var.get():
                self.key_var.set("3 3 2 5")
            self.key_entry.config(state="normal")
        elif algo == "Transposition":
            self.key_label.config(text="Kunci (kata):")
            self.key_entry.config(state="normal")
        elif algo == "ROT13":
            self.key_label.config(text="(tanpa kunci)")
            self.key_var.set("")
            self.key_entry.config(state="disabled")

    def _process(self):
        text = self.input_txt.get("1.0", "end-1c")
        algo = self.selected_algo.get()
        key = self.key_var.get()
        mode = self.mode.get()
        try:
            if algo == "Caesar":
                func = caesar.encrypt if mode == "encrypt" else caesar.decrypt
                result = func(text, key)
            elif algo == "Vigenère":
                func = vigenere.encrypt if mode == "encrypt" else vigenere.decrypt
                result = func(text, key)
            elif algo == "Hill (2x2)":
                func = hill.encrypt if mode == "encrypt" else hill.decrypt
                result = func(text, key)
            elif algo == "Transposition":
                func = transposition.encrypt if mode == "encrypt" else transposition.decrypt
                result = func(text, key)
            elif algo == "ROT13":
                # same function both ways
                result = rot13.encrypt(text, "")
            else:
                raise ValueError("Algoritma tidak dikenal.")
            self.output_txt.config(state="normal")
            self.output_txt.delete("1.0", "end")
            self.output_txt.insert("1.0", result)
            self.status_var.set(f"Selesai {mode} dengan {algo}.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Terjadi error.")

    def _clear(self):
        self.input_txt.delete("1.0", "end")
        self.output_txt.delete("1.0", "end")
        self.status_var.set("Dibersihkan.")

    def run(self):
        self.root.mainloop()
