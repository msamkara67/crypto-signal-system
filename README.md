# 🤔 Crypto Signal System

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

---

## 📂 Archive

Contains only deprecated or inactive scripts (e.g. `data_analysis.py`) kept for reference but not used in production.

---

## 🧑‍💻 Author


Muhammet Samkara  
[GitHub](https://github.com/msamkara67)

---

