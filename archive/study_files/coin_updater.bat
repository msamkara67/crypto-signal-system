@echo off

chcp 65001 >nul

echo [0] Tarih bilgisi alınıyor ve template güncelleniyor...
start /wait "" C:\Anaconda\pythonw.exe "C:\Users\Muhammet Samkara\Desktop\coin_Updater\update_template_date.py"

echo.
echo [1] Anaconda Python ile coin_updater_debug.py başlatılıyor...
C:\Anaconda\python.exe "C:\Users\Muhammet Samkara\Desktop\coin_Updater\coin_updater_debug.py"

echo.
echo [2] Anaconda Python ile signal_generator.py başlatılıyor...
C:\Anaconda\python.exe "C:\Users\Muhammet Samkara\Desktop\Borsa Kripto\signal_generator.py"

pause






