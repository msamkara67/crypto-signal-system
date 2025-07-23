import xlwings as xw
import os
import shutil

# --- Dosya yolları ---
base_path = r"C:\Users\Muhammet Samkara\Desktop\coin_Updater"
source_file = os.path.join(base_path, "coin_data_180days_top100.xlsx")
target_dir = os.path.join(base_path, "back_up")
target_file = os.path.join(target_dir, "coin_data_180days_top100.xlsm")

# --- Hedef klasör yoksa oluştur ---
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# --- Dosyayı xlsm formatında kopyala (içerik bozulmadan) ---
app = xw.App(visible=False)
wb = app.books.open(source_file)

try:
    wb.save(target_file)  # xlsm formatına dönüştürerek kaydet
    wb.close()
    app.quit()
except Exception as e:
    wb.close()
    app.quit()
    raise RuntimeError(f"❌ Dosya kaydetme hatası: {e}")

# --- VBA makro: grafik alanlarını şeffaf yap ---
vba_code = """
Sub MakeAllChartsTransparent()
    Dim ws As Worksheet
    Dim chObj As ChartObject
    Dim shp As Shape

    For Each ws In ThisWorkbook.Worksheets
        For Each chObj In ws.ChartObjects
            With chObj.Chart
                .ChartArea.Format.Fill.Visible = msoFalse
                .PlotArea.Format.Fill.Visible = msoFalse
            End With
        Next chObj

        For Each shp In ws.Shapes
            If shp.Type = msoChart Then
                With shp.Chart
                    .ChartArea.Format.Fill.Visible = msoFalse
                    .PlotArea.Format.Fill.Visible = msoFalse
                End With
            End If
        Next shp
    Next ws
End Sub
"""

# --- VBA ekle ve çalıştır ---
app = xw.App(visible=False)
wb = app.books.open(target_file)

try:
    wb.api.VBProject.VBComponents.Add(1).CodeModule.AddFromString(vba_code)
    wb.macro("MakeAllChartsTransparent")()
    wb.save()
    print("✅ Başarıyla .xlsm olarak kaydedildi, VBA eklendi ve grafikler şeffaflaştırıldı.")
except Exception as e:
    print(f"❌ VBA işlemi sırasında hata oluştu: {e}")
finally:
    wb.close()
    app.quit()




