import os
import xlwings as xw
from datetime import datetime
from config import working_dir_name

# Giriş ve çıkış yolları
desktop = os.path.expanduser("~/Desktop")
base_dir = working_dir_name
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

    # VBA kodu (şeffaflık + Chart6 için Y ekseni otomatik ayar)
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

    Sub AutoScaleYAxis_Chart6()
    Dim ws As Worksheet
    Dim ch As ChartObject
    
    Set ws = Sheets("Graphs")
    
    Dim cht As ChartObject
    Set cht = Sheets("Graphs").ChartObjects("Chart 6")
    
    Dim s As Series
    Dim i As Long, j As Long
    Dim minVal As Double, maxVal As Double
    Dim vVals As Variant

    ' Baslangiç degerleri
    minVal = 1E+30
    maxVal = -1E+30
    
    ' Tüm serilerin verilerine göre min-max hesapla
    For Each s In cht.Chart.SeriesCollection
        On Error Resume Next
        vVals = s.Values
        For j = LBound(vVals) To UBound(vVals)
            If IsNumeric(vVals(j)) Then
                If vVals(j) < minVal Then minVal = vVals(j)
                If vVals(j) > maxVal Then maxVal = vVals(j)
            End If
        Next j
        On Error GoTo 0
    Next s

    ' Küçük bir buffer ekle (istege bagli)
    Dim buffer As Double
    buffer = (maxVal - minVal) * 0.05

    ' Eksenleri ayarla
    With cht.Chart.Axes(xlValue)
        .MinimumScale = minVal - buffer
        .MaximumScale = maxVal + buffer
    End With

    End Sub
    '''

    # VBA modülü oluştur ve kodları ekle
    wb.api.VBProject.VBComponents.Add(1).CodeModule.AddFromString(vba_code)

    # .xlsm olarak kaydet
    wb.save(xlsm_path)

    # Her iki makroyu çalıştır
    app.macro("MakeChartsTrulyTransparent")()
    # app.macro("AutoScaleYAxis_Chart6")()

    # Fazladan açılmış Book1 varsa kapat
    for book in app.books:
        if book.name == "Book1":
            book.close()

    # Dosyayı görünür yap ve açık bırak
    app.visible = True
    wb.activate()
    print(f"✅ {new_filename} oluşturuldu, makrolar uygulandı ve dosya açık bırakıldı.")

except Exception as e:
    print(f"❌ Hata oluştu: {e}")
    wb.close(save=False)
    app.quit()









