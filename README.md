 🤔 Crypto Signal System

A Python-based technical analysis framework that integrates **Excel**, **RSI logic**, and **automated data gathering** to generate crypto trading signals.

---

## 📁 Project Structure

```
coin_updater_step2.py      # Main automation script: fetches daily close & volume data and updates Excel files
XLSM_version.py            # Presentation-oriented version that also creates archive and backup files (macro-enabled)
date_picker.py             # GUI interface (Tkinter) to choose target date for data update
coin_data_180days_top100.xlsx   # Main analysis file with historical crypto data and RSI-based signal logic
coin_data_template.xlsx         # Temporary staging file populated by fetched data before transfer
archive/                   # Contains only deprecated or inactive scripts
```

---

## ⚙️ How It Works

1. User selects a target date using the `date_picker.py` interface.
2. `coin_updater_step2.py` fetches **closing prices and volume** data for the top coins (e.g. via yfinance).
3. This data is first written into `coin_data_template.xlsx`, then transferred into `coin_data_180days_top100.xlsx`.
4. RSI signals, volatility, and volume-based alerts are then generated automatically in Excel.


![Crypto Signal System Flow](https://raw.githubusercontent.com/msamkara67/crypto-signal-system/main/docs/Signal_System_Flow.png)
---

## 🛠 Features

- Daily close & volume data fetching (e.g. from yfinance)
- RSI threshold logic (BUY, SELL, CAUTION levels)
- 3-day RSI stress analysis (volatility)
- 5-day average volume-based spike alerts
- GUI-based date picker
- Excel–Python integration, full automation

---

## 🚧 To Do

- Modular backtesting engine
- Trade simulator with logging
- Interactive dashboard (optional, e.g. Streamlit)


Usage
date_picker.py dosyasını çalıştırarak tarih seçin:

bash
Copy
Edit
python date_picker.py
Seçilen tarih otomatik olarak alınır ve:

Kapanış ve hacim verileri toplanır (coin_updater_step2.py)

Geçici coin_data_template.xlsx dosyasına kaydedilir

Ardından coin_data_180days_top100.xlsx dosyasına transfer edilir

RSI sinyalleri ve analizler Excel üzerinden otomatik hesaplanır

Güncel dosyalar:

XLSM_version.py dosyası üzerinden sunum/raporlama amaçlı .xlsm versiyon oluşturulur

Yedekleme ve arşivleme işlemleri yapılır

Not: Kodların düzgün çalışması için Excel dosyalarının kapalı olması gerekir.
---

## 📂 Archive

Contains only deprecated or inactive scripts (e.g. `data_analysis.py`) kept for reference but not used in production.

---

## 🧑‍💻 Author


Muhammet Samkara  
[GitHub](https://github.com/msamkara67)

---

