# 🎯 Prediksi Tingkat Obesitas Menggunakan Machine Learning

Capstone Project – Bengkel Koding Data Science  
Universitas Dian Nuswantoro  

---

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk membangun model klasifikasi yang mampu memprediksi **tingkat obesitas** seseorang berdasarkan informasi fisik, kebiasaan makan, dan gaya hidup. Model yang dibangun dideploy dalam bentuk aplikasi web interaktif menggunakan **Streamlit**.

---

## 🧠 Metodologi

1. **Exploratory Data Analysis (EDA)**
   - Analisis distribusi data
   - Deteksi outlier, missing value, dan ketidakseimbangan kelas

2. **Preprocessing**
   - Penanganan missing value dan outlier
   - Encoding fitur kategorikal
   - Normalisasi data
   - Oversampling dengan SMOTE

3. **Modeling & Evaluation**
   - Model: KNN, Decision Tree, Random Forest
   - Evaluasi: Akurasi, Presisi, Recall, F1-Score
   - Confusion Matrix & Visualisasi Perbandingan

4. **Hyperparameter Tuning**
   - GridSearchCV untuk menemukan parameter optimal

5. **Deployment**
   - Aplikasi dibangun dengan **Streamlit**
   - Model disimpan menggunakan `joblib` dan dideploy ke **Streamlit Cloud**

---
## 🗂️ File di Repo

| File | Deskripsi |
|------|-----------|
| `app.py` | Aplikasi utama berbasis Streamlit |
| `model_obesitas.pkl` | Model klasifikasi terlatih (Random Forest) |
| `scaler.pkl` | Scaler untuk normalisasi input pengguna |
| `requirements.txt` | Library yang dibutuhkan agar aplikasi berjalan |
| `README.md` | Deskripsi proyek ini |

---

## 🚀 Cara Menjalankan Aplikasi

### 🔹 Secara Lokal
```bash
pip install -r requirements.txt
streamlit run app.py

```

🔹 Versi Online (Streamlit Cloud)
👉 Klik di sini : https://deployfastauas.streamlit.app/
