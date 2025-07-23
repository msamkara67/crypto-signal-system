import sys
import os
import shutil
from datetime import datetime, timedelta
from openpyxl import load_workbook

# Ana dosya yolu
data_path = r"C:\Users\Muhammet Samkara\Desktop\coin_Updater\coin_data_180days_top100.xlsx"

# 1. Argümandan tarihi al
if len(sys.argv) < 2:
    raise ValueError("⛔ Lütfen geçerli bir tarih girin. Örnek: 2025-07-18")

try:
    input_date = datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
except ValueError:
    raise ValueError("⛔ Tarih formatı geçersiz. Doğru format: YYYY-MM-DD")

# 1 gün öncesine git
previous_date = input_date - timedelta(days=1)
date_str = previous_date.strftime("%Y-%m-%d")

# Hedef klasör ve dosya adı
archive_folder = r"C:\Users\Muhammet Samkara\Desktop\coin_Updater\archive"
target_filename = f"Daily_Market_{date_str}.xlsx"
target_path = os.path.join(archive_folder, target_filename)

# Dosya zaten varsa sil
if os.path.exists(target_path):
    try:
        os.remove(target_path)
        print(f"🗑️ Eski yedek silindi: {target_filename}")
    except Exception as e:
        print(f"⚠️ Eski yedek silinemedi: {e}")

# Dosyayı kopyala
try:
    shutil.copyfile(data_path, target_path)
    print(f"📦 Yedekleme tamamlandı: {target_filename}")
except Exception as e:
    print(f"❌ Yedekleme sırasında hata oluştu: {e}")





