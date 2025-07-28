import os
import xlwings as xw
from datetime import datetime

# Giriş ve çıkış yolları
desktop = os.path.expanduser("~/Desktop")
base_dir = os.path.join(desktop, "coin_Updater")
src_file = os.path.join(base_dir, "coin_data_180days_top100.xlsx")
backup_dir = os.path.join(base_dir, "back_up")

# Excel dosyasını aç (başlangıçta görünmez)
app = xw.App(visible=False)
wb = app.books.open(src_file)

try:
    # RSI sayfasından tarih al
    rsi_sheet = wb.sheets['RSI']
    date_val = rsi_sheet.range("N2").value

    # Tarihi formatla
    if isinstance(date_val, datetime):
        formatted_date = date_val.strftime("%Y-%m-%d")
    else:
        formatted_date = str(date_val)

    # Yeni dosya adı ve yolu
    new_filename = f"Binance_{formatted_date}.xlsm"
    xlsm_path = os.path.join(backup_dir, new_filename)

    # VBA kodu (grafik şeffaflığı)
    vba_code = '''
    Sub MakeChartsTrulyTransparent()
        Dim ws As Worksheet
        Dim ch As ChartObject
        For Each ws In ThisWorkbook.Worksheets
            For Each ch In ws.ChartObjects
                With ch.Chart.PlotArea.Format.Fill
                    .Visible = msoTrue
                    .ForeColor.RGB = RGB(0, 0, 0)
                    .Transparency = 1
                End With
                With ch.Chart.ChartArea.Format.Fill
                    .Visible = msoTrue
                    .ForeColor.RGB = RGB(0, 0, 0)
                    .Transparency = 1
                End With
            Next ch
        Next ws
    End Sub
    '''

    # Makro modülü oluştur
    wb.api.VBProject.VBComponents.Add(1).CodeModule.AddFromString(vba_code)

    # .xlsm olarak kaydet
    wb.save(xlsm_path)

    # VBA makroyu çalıştır
    app.macro("MakeChartsTrulyTransparent")()

    # Fazladan açılmış Book1 varsa kapat
    for book in app.books:
        if book.name == "Book1":
            book.close()

    # Dosyayı görünür yap ve açık bırak
    app.visible = True
    wb.activate()
    print(f"✅ {new_filename} oluşturuldu, makro uygulandı ve dosya açık bırakıldı.")

except Exception as e:
    print(f"❌ Hata oluştu: {e}")
    wb.close(save_changes=False)
    app.quit()








