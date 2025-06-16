import streamlit as st
import pickle
import numpy as np

# === Load model ===
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# === Styling CSS ===
st.markdown("""
    <style>
    [data-testid="stHeader"] {
        display: none;
    }
    .main-container {
        background-color: #0f172a;
        color: #f1f5f9;
        font-family: 'Segoe UI', sans-serif;
        max-width: 800px;
        margin: auto;
        padding: 2rem 3rem;
        border-radius: 16px;
    }
    h1 {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    h3 {
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    p {
        margin-bottom: 2rem;
        color: #cbd5e1;
    }
    </style>
""", unsafe_allow_html=True)

# === Container Utama ===
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# === Judul ===
st.markdown("## Prediksi Tingkat Obesitas")
st.write("Masukkan data diri dan kebiasaan Anda dengan lengkap untuk memprediksi tingkat obesitas berdasarkan model terpercaya.")

# === Form Input ===
st.markdown("### Informasi Pribadi dan Kebiasaan")

umur = st.number_input("Umur (tahun)", min_value=5, max_value=100, value=30)
tinggi = st.number_input("Tinggi badan (cm)", min_value=100, max_value=250, value=170)
berat = st.number_input("Berat badan (kg)", min_value=30, max_value=200, value=70)
aktivitas_fisik = st.slider("Frekuensi aktivitas fisik (hari/minggu)", 0, 7, 3)
makan_cepat_saji = st.selectbox("Seberapa sering makan fast food?", ["Tidak pernah", "Jarang", "Sering"])
minum_air = st.slider("Jumlah air minum per hari (gelas)", 0, 15, 8)
merokok = st.radio("Apakah Anda merokok?", ["Ya", "Tidak"])

# === Encoding manual ===
ff_map = {"Tidak pernah": 0, "Jarang": 1, "Sering": 2}
smoke_map = {"Ya": 1, "Tidak": 0}

# === Prediksi ===
if st.button("Prediksi"):
    tinggi_m = tinggi / 100
    bmi = berat / (tinggi_m ** 2)

    features = np.array([
        umur,
        berat,
        tinggi,
        aktivitas_fisik,
        ff_map[makan_cepat_saji],
        minum_air,
        smoke_map[merokok],
        bmi
    ]).reshape(1, -1)

    pred = model.predict(features)[0]

    # Menampilkan hasil
    st.markdown("### Hasil Prediksi:")
    st.success(f"Tingkat obesitas Anda diprediksi sebagai: **{pred}**")

# === Tutup container ===
st.markdown('</div>', unsafe_allow_html=True)
