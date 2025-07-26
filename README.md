# Crypto Signal System

A Python + Excel + VBA hybrid system that automatically generates technical analysis charts and buy/sell signals for top cryptocurrencies using 6-month RSI, Moving Averages, and Volume trends.

---

## 🔎 Overview

This project automates the collection, analysis, and visualization of crypto market data. It uses Python scripts to fetch live or historical data from **Yahoo Finance**, processes it through Excel, and finally produces:

* RSI, MA7, MA25, MA99 charts
* Volume & Volatility trends
* Automated Buy/Sell signal labeling

The final output is a polished Excel dashboard (with embedded macros and dynamic charts) ready for daily review or backtesting.

---

## 🪄 Features

* ✅ Fully automated data update pipeline
* ✅ RSI alert system with threshold classification
* ✅ MA crossover detection (Golden/Death Cross)
* ✅ Volume and volatility tagging
* ✅ Dynamic Excel dashboard per coin
* ✅ Data archive system with daily XLSM exports

---

## 🌐 How It Works

### 1. User picks a date

Run `date_picker.py` → User selects a target date.

### 2. Main script: `coin_updater_step2.py`

* Reads the selected date
* Fetches data from Yahoo Finance
* Fills `coin_data_template.xlsx`
* Transfers data to `coin_data_180days_top100.xlsx`
* Calls `XLSM_version.py` to:

  * Inject VBA for chart cleanup
  * Save and archive new XLSM file
  * Open the result automatically

---

## 📈 Outputs

* `coin_data_180days_top100.xls[x/m]` → Your main signal engine
* `Charts` page → Dynamic visuals by coin
* `RSI` page → Categorized RSI/MA/Volume/Volatility alerts
* Archived Excel report per update in `/archive`
  
<img width="1558" height="773" alt="image" src="https://github.com/user-attachments/assets/0023e440-e440-43bb-9248-5d15c11858d4" />


---

## 📁 Repo Structure

```
crypto-signal-system/
├── coin_updater_step2.py
├── date_picker.py
├── XLSM_version.py
├── utils/           # Helper functions
├── data/
│   ├── coin_data_template.xlsx
│   └── coin_data_180days_top100.xlsx
├── archive/         # Saved XLSM files
└── README.md
```

---

## 🔧 Requirements

* Python 3.x
* openpyxl, pandas, yfinance, pywin32
* Excel with macro support (Windows-only)

---

## 🎨 Sample Preview

*(Screenshots can be added here later)*

---

## 🧠 Kullanım Senaryosu (Use Case)

Bu sistem şunlar için idealdir:

* 📈 RSI, hacim ve ortalama gibi göstergeleri baz alarak al-sat stratejisi üretmek isteyen yatırımcılar
* 💼 Grafikle uğraşmadan analiz yapmak isteyen ama veri setlerini canlı test etmekten keyif alanlar
* 🧪 “Geçmişte bu sinyal çalışmış mı?” sorusuna veriye dayalı cevap arayanlar
* 🤖 Basit ama genişletilebilir bir sistem üzerinde kendi fikirlerini denemek isteyen geliştirici adayları
* 📊 Excel'i bırakmak istemeyen ama Python'un gücünden de faydalanmak isteyen hibrit kullanıcılar

> Sistem, sabit değil. Kullanıcıya göre evrilir.
> Hangi analiz senin işine yarıyorsa, sistem onu sunar.
> İster grafik üret, ister sinyal logla, ister ileri analiz için dışa aktar.
> Kod senin, veri senin, karar da senin.

---

## 🚀 To Do

*

---

## 🤝 Author

Developed by [@msamkara67](https://github.com/msamkara67) ✨

---

> "Not a full developer? Doesn’t matter. Build the system you wish existed."

---

