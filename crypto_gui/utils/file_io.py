
from tkinter import filedialog, messagebox

def import_text_to(widget):
    path = filedialog.askopenfilename(
        title="Import .txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not path:
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()
        widget.delete("1.0", "end")
        widget.insert("1.0", data)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membaca file:\n{e}")

def export_text_from(widget):
    path = filedialog.asksaveasfilename(
        title="Simpan ciphertext ke .txt",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if not path:
        return
    try:
        data = widget.get("1.0", "end-1c")
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan file:\n{e}")
