  # 📊 Crypto Signal System

**Crypto Signal System**, Python + Excel + VBA işbirliğiyle çalışan, kullanıcı etkileşimli bir teknik analiz ve otomatik sinyal üretim sistemidir. 180 günlük geçmiş veriye dayanarak RSI, hacim, hareketli ortalamalar ve volatilite gibi göstergelerle işlem kararlarını destekleyen grafikler ve uyarılar üretir.

---

## ⚙️ Sistem Özeti

- 🔄 **Günlük Otomatik Veri Güncelleme**  
  Canlı sistemden (`yfinance`) coin kapanış fiyatlarını ve hacim verilerini çeker.

- 📅 **Tarih Seçimli İşlem**  
  Canlı veya geçmiş tarihli analiz yapılabilir. `date_picker.py` ile tarih kullanıcıdan alınır.

- 🧠 **RSI ve MA Bazlı Otomatik Sinyal Üretimi**  
  RSI14 değerine göre 5 seviyeli sinyal üretimi (Buy, Warming Up, Be Cautious, Sell, etc).  
  MA7 / MA25 / MA99 üzerinden Golden Cross ve Death Cross uyarıları.

- 📈 **Dinamik Grafikleme**  
  Her coin için grafikler otomatik oluşturulur ve xlsm formatında arşivlenir.

- 💾 **Otomatik Arşivleme**  
  Grafikler gün sonu `.xlsm` dosyasına kaydedilir, geçmişe dönük inceleme yapılabilir.

---

## 🧩 Script Yapısı

### 🔹 `coin_updater_step2.py` → 🔄 Ana script  
- Veriyi çeker, `coin_data_template.xlsx`’e yazar.  
- Ardından `coin_data_180days_top100.xlsx` dosyasına aktarır.  
- Grafik oluşturma için `XLSM_version.py` scriptini tetikler.

### 🔹 `date_picker.py`  
- Kullanıcıdan tarih alır → geçici Excel dosyasına yazar.

### 🔹 `XLSM_version.py`  
- Grafik şablonlarını dinamik VBA koduyla günceller.  
- Çıktıyı `.xlsm` dosyası olarak arşivler ve kullanıcıya sunar.

---

## 📊 Örnek Sinyal Çıktısı

| Coin | RSI14 | RSI Alert | Volatility | MA7/MA99 |
|------|-------|-----------|------------|----------|
| BTC  | 49.22 | —         | -20.47     | 1.11     |
| ETH  | 83.68 | SELL      | -3.48      | 1.46     |
| BNB  | 89.24 | SELL      | -3.26      | 1.17     |

> 🔍 Grafik sayfası üzerinden her coin’in detaylı teknik geçmişi incelenebilir.

---

## 🧠 Proje Amacı

Bu sistem:
- Algoritmik düşünceyle teknik veriyi görselleştirmek,
- Kullanıcıyı yorum yükünden kurtarmak,
- Geçmiş sinyal döngülerini analiz edip canlıda test etmeyi amaçlamaktadır.
- 
---
## 👤 Geliştirici

📌 **[msamkara67](https://github.com/msamkara67)**  
Bu proje bir mühendislik ve gözlem ürünü olup Python, Excel ve algoritmik analiz becerilerini birleştirir.

---

## 📂 Dosya Yapısı (File Structure)

Bu proje aşağıdaki temel dosya ve klasör yapısına sahiptir:
```
crypto-signal-system/
│
├── coin_updater_step2.py # Ana script; tüm güncelleme ve analiz sürecini başlatır.
├── date_picker.py # Kullanıcıdan tarih alır ve ara dosyaya yazar.
├── XLSM_version.py # Grafik düzenleme VBA kodunu oluşturur ve çalıştırır.
│
├── coin_data_template.xlsx # Güncel verilerin ilk yazıldığı geçici ara dosya.
├── coin_data_180days_top100.xlsm # Ana analiz dosyası; grafikler, sinyaller ve veriler burada toplanır.
│
├── auto_run.bat # Ana scripti çalıştırmak için kullanılabilecek BAT dosyası.
└── README.md # Proje açıklamaları ve kullanım dokümantasyonu.
```
> 💡 *Not: Excel dosyaları VBA makroları içerdiğinden `.xlsm` uzantısıyla çalışır.*

---

## 💡 Sistemin İşleyişi (How It Works)

Bu sistem, Python scriptleri, Excel ve VBA'nın birlikte çalıştığı hibrit bir mimaride geliştirilmiştir. Kullanıcıdan bir tarih alınarak:

1. İlgili güne ait coin kapanış fiyatları ve işlem hacmi sistemden çekilir.
2. Bu veriler geçici bir ara dosyada toplanır ve ardından analiz dosyasına aktarılır.
3. Excel tarafında RSI, hacim ve hareketli ortalamalara dayalı teknik analizler gerçekleştirilir.
4. Otomatik olarak al/sat sinyalleri üretilir ve coin bazlı grafikler oluşturulur.
5. VBA ile grafikler dinamik olarak formatlanır ve `.xlsm` uzantılı arşiv dosyası oluşturulur.

Bu yapı sayesinde geçmiş sinyaller analiz edilebilir, grafiksel takibi kolaylaştırılır ve algoritmik düşünce test edilebilir hale gelir.

---

## 📌 Kullanım (Usage)
Bu sistem, kullanıcıdan bir tarih alarak o tarihe ait coin kapanış fiyatı ve hacim verilerini çeker ve otomatik sinyal analizleriyle Excel üzerinde sunar.

✅ Adımlar:
Ana scripti çalıştırın:

python coin_updater_step2.py
Açılan arayüzde işlem yapılmak istenen tarihi seçin ve onaylayın.

Sistem şu işlemleri otomatik olarak yapar:

Seçilen tarihin verilerini canlı olarak yfinance üzerinden çeker.

Verileri önce coin_data_template.xlsx dosyasına yazar.

Ardından bu verileri analiz dosyası olan coin_data_180days_top100.xlsx dosyasına aktarır.

RSI, MA ve hacim tabanlı sinyallerin üretimini tetikler.

Günlük grafikler için dinamik VBA kodları oluşturur ve .xlsm formatında arşiv dosyası üretir.

Günlük analiz dosyasını otomatik olarak açar.

Sonuç:

coin_data_180days_top100.xlsx → Güncel sinyal tablosu

coin_data_YYYYMMDD.xlsm → O güne özel grafik arşivi
  
Tüm işlemler Python, Excel ve VBA’nın birlikte çalıştığı hibrit bir mimaride gerçekleşir

---
## 📊 Örnek Çıktılar (Sample Outputs)

Sistem çalıştırıldığında, her coin için hem teknik sinyaller hem de grafiksel analiz çıktıları otomatik üretilir.

### 1. Teknik Sinyal Tablosu

Aşağıda, RSI değerlerine göre oluşturulmuş bir sinyal tablosu örneği yer almaktadır:

![RSI Signal Table](https://github.com/msamkara67/crypto-signal-system/assets/xxxxx/RSI-sample.png)

### 2. Grafik Çıktısı

Coin bazlı grafiklerde RSI, fiyat, hacim, MA değerleri ve volatilite analizi birlikte görselleştirilir:

![WLD Graph](https://github.com/msamkara67/crypto-signal-system/assets/yyyyy/WLD-graph-sample.png)

---
## ✅ Notlar

- 🔒 Tüm dosyalar yerelde çalışmak üzere yapılandırılmıştır.  
- 📂 Arşivlenen `.xlsm` dosyaları her gün otomatik olarak oluşturulur.
- 🧪 Sinyaller şu anda test aşamasındadır, yatırım tavsiyesi değildir.

---

## 📬 İletişim

Proje hakkında daha fazla bilgi ya da katkı için iletişime geçebilirsiniz.
