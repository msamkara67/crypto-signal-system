@echo off
cd /d "C:\Users\Muhammet Samkara\Desktop\coin_Updater"
del date_input_result.txt >nul 2>&1

echo [0] Tarih bilgisi alınıyor...
start /wait C:\Anaconda\python.exe "date_popup_and_trigger.py"

REM Geçici dosyayı oku
setlocal ENABLEDELAYEDEXPANSION
set RESULT=
for /f "delims=" %%a in (date_input_result.txt) do set RESULT=%%a

if "%RESULT%"=="CANCEL" (
    echo ❌ Kullanıcı iptal etti. Çıkılıyor...
    exit /b
)

if "%RESULT%"=="INVALID" (
    echo ⛔ Geçersiz tarih formatı girildi. Çıkılıyor...
    exit /b
)

echo ✅ Tarih başarıyla alındı. Güncellemeye devam ediliyor...

echo [1] coin_updater_debug.py başlatılıyor...
C:\Anaconda\python.exe "coin_updater_debug.py"

echo [2] signal_generator.py başlatılıyor...
C:\Anaconda\python.exe "C:\Users\Muhammet Samkara\Desktop\Borsa Kripto\signal_generator.py"

pause


