import os
import shutil
from datetime import datetime
from openpyxl import load_workbook

# === Ayarlar ===
base_path = r"C:\Users\Muhammet Samkara\Desktop\coin_Updater"
source_file = os.path.join(base_path, "coin_data_180days_top100.xlsx")

# === Tarihi RSI sayfasındaki N2 hücresinden al
wb = load_workbook(source_file, data_only=True)
rsi_sheet = wb["RSI"]
date_cell = rsi_sheet["N2"].value

if not isinstance(date_cell, datetime):
    raise ValueError("N2 hücresindeki değer geçerli bir tarih değil!")

selected_date = date_cell.date()
folder_name = selected_date.strftime("%Y-%m-%d")
wb.close()

# === Klasör Oluştur (varsa silip yeniden oluştur)
archive_folder = os.path.join(base_path, "archive", folder_name)

if os.path.exists(archive_folder):
    shutil.rmtree(archive_folder)
os.makedirs(archive_folder)

# === 1. Formüllü versiyon
formullu_target_path = os.path.join(archive_folder, f"Market_Values_{folder_name}.xlsx")
shutil.copy2(source_file, formullu_target_path)
print(f"📄 Formüllü dosya kopyalandı → {formullu_target_path}")






