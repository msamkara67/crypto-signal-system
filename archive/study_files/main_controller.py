import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
import subprocess
import os

# === Tarih Seçim Popup ===
def select_date():
    def on_ok():
        selected_date = cal.selection_get()
        root.destroy()
        run_updater(selected_date)

    root = tk.Tk()
    root.title("Tarih Seçimi")

    cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(padx=10, pady=10)

    ok_button = tk.Button(root, text="Tamam", command=on_ok)
    ok_button.pack(pady=(0, 10))

    root.mainloop()

# === Updater Scripti Çalıştır ===
def run_updater(selected_date):
    print("[0] Tarih seçimi popup'ı başlatıldı.")
    print(f"[1] Seçilen tarih: {selected_date}")
    print(f"[1] İşleme alınan tarih: {selected_date}")

    updater_script_path = r"C:\Users\Muhammet Samkara\Desktop\coin_Updater\coin_updater_debug.py"

    if not os.path.exists(updater_script_path):
        messagebox.showerror("Hata", f"Script bulunamadı: {updater_script_path}")
        return

    try:
        subprocess.run(['python', updater_script_path, selected_date.strftime("%Y-%m-%d")], check=True)
    except subprocess.CalledProcessError as e:
        print(e)
        messagebox.showerror("Hata", "Script çalışırken bir hata oluştu.")

if __name__ == "__main__":
    select_date()


