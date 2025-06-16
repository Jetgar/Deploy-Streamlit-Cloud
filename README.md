# Prediksi Tingkat Obesitas Menggunakan Machine Learning 

---

## Ringkasan Proyek
Proyek ini fokus pada pembangunan sebuah model klasifikasi yang mampu menentukan kategori tingkat obesitas seseorang berdasarkan data terkait kondisi fisik, kebiasaan makan, serta gaya hidup. Model ini kemudian diwujudkan dalam aplikasi web interaktif dengan memanfaatkan **Streamlit**.

---

## Langkah Pengerjaan
**Analisis Data Awal (Exploratory Data Analysis)**
- Memahami sebaran dan karakteristik data
- Mengidentifikasi outlier, data yang hilang, dan potensi ketidakseimbangan kelas

**Persiapan Data**
- Mengatasi nilai data yang hilang dan penyimpangan (outlier)
- Mengonversi fitur kategorikal menjadi format numerik
- Melakukan normalisasi agar data siap dimodelkan
- Mengaplikasikan teknik oversampling SMOTE untuk mengatasi kelas minoritas

**Pengembangan Model dan Evaluasi**
- Menggunakan algoritma KNN, Decision Tree, dan Random Forest untuk klasifikasi
- Menilai performa model menggunakan metrik seperti akurasi, presisi, recall, dan F1-score
- Menampilkan matriks kebingungan dan membandingkan hasil antar model secara visual

**Optimalisasi Model (Hyperparameter Tuning)**
- Menentukan parameter terbaik dengan metode GridSearchCV agar akurasi meningkat

**Implementasi Aplikasi**
- Mengembangkan aplikasi berbasis Streamlit yang user-friendly
- Menyimpan model terlatih dan scaler menggunakan joblib
- Deploy aplikasi ke Streamlit Cloud untuk akses online

---
## Struktur File dalam Repository

| File | Deskripsi |
|------|-----------|
| `ObesityDataSet.csv` | Dataset yang digunakan untuk melatih model klasifikasi obesitas |
| `README.md` | Dokumen penjelasan detail tentang proyek |
| `appp.py` | Script utama aplikasi interaktif berbasis Streamlit |
| `requirements.txt` | Daftar paket Python yang dibutuhkan untuk menjalankan aplikasi |

---

## Panduan Menjalankan Aplikasi

### Langkah-langkah Mengoperasikan secara Lokal:
```bash
pip install -r requirements.txt
streamlit run app.py

```

Versi Aplikasi Online (Via Streamlit Cloud):
[Klik di sini untuk akses langsung](https://deployobesity.streamlit.app/)
