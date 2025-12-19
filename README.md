# 🌸 Scent Consultant AI

**Temukan Karakter Aroma yang Mendefinisikan Dirimu.**

Scent Consultant AI adalah aplikasi cerdas yang bertindak sebagai "Master Perfumer" pribadi Anda. Menggunakan kekuatan **Google Gemini 2.5 Flash**, aplikasi ini menganalisis kepribadian, momen, dan preferensi Anda untuk meracik rekomendasi parfum yang sangat spesifik dan personal.

Dibangun dengan **FastAPI** di backend untuk pemrosesan AI yang cepat, dan antarmuka web elegan yang memberikan pengalaman selayaknya berkonsultasi di butik parfum mewah.

---

## ✨ Fitur Utama

* **🧠 AI Master Perfumer:** Menggunakan prompt engineering khusus pada model **Gemini 2.5 Flash** untuk meniru gaya bicara dan keahlian seorang ahli parfum berpengalaman 20 tahun.
* **🔍 Analisis Olfaktori Mendalam:** Tidak hanya merekomendasikan merek, AI menganalisis hubungan antara *notes* parfum (Top, Heart, Base) dengan kepribadian dan cuaca saat penggunaan.
* **🎨 Elegant User Interface:** Desain antarmuka yang mewah dengan palet warna *Cream & Gold*, font tipografi klasik (*Cormorant Garamond*), dan latar belakang artistik.
* **⚡ Real-time Recommendation:** Memberikan output dalam format JSON terstruktur yang langsung dirender menjadi tampilan visual yang rapi tanpa loading lama.
* **📱 Responsive Design:** Tampilan yang tetap cantik dan fungsional baik di Laptop maupun Smartphone.

---

## 🛠️ Teknologi yang Digunakan

### Backend
* **Python 3.11**
* **FastAPI:** Framework modern untuk membangun API berkinerja tinggi.
* **Google Generative AI (Gemini):** Otak utama di balik rekomendasi cerdas.
* **Pydantic:** Validasi data input pengguna.
* **Uvicorn:** ASGI Server untuk menjalankan aplikasi Python.

### Frontend
* **HTML5 & CSS3:** Desain custom tanpa framework CSS berat.
* **JavaScript (Vanilla):** Menangani logika form dan komunikasi ke API.
* **Google Fonts:** Menggunakan *Cormorant Garamond* dan *Montserrat* untuk tipografi.

---

## 📂 Struktur Project

```text
.
├── backend/
│   └── main.py            # Server utama FastAPI & Logika Gemini AI
├── index.html             # Halaman utama aplikasi (Frontend)
├── style.css              # Styling CSS (Tema Mewah/Gold)
├── requirements.txt       # Daftar library Python yang dibutuhkan
├── Gemini_Generated_Image.png # Aset Background
├── .env                   # (Harus dibuat) File konfigurasi API Key
└── README.md              # Dokumentasi Project
