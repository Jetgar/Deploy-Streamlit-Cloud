import streamlit as st
import numpy as np
import joblib

# Load model dan scaler
model = joblib.load("model_obesitas.pkl")
scaler = joblib.load("scaler.pkl")

# Judul Aplikasi
st.title("Prediksi Tingkat Obesitas")
st.markdown("Masukkan data berikut untuk memprediksi tingkat obesitas:")

# Input data
age = st.number_input("Usia", 10, 100, 25)
height = st.number_input("Tinggi Badan (meter)", 1.0, 2.5, 1.70)
weight = st.number_input("Berat Badan (kg)", 30, 200, 70)
fcvc = st.slider("Konsumsi Sayur (FCVC)", 1, 3, 2)
ncp = st.slider("Jumlah Makan per Hari (NCP)", 1, 4, 3)
ch2o = st.slider("Minum Air (CH2O)", 1, 3, 2)
faf = st.slider("Aktivitas Fisik (FAF)", 0, 3, 1)
tue = st.slider("Waktu Pakai Teknologi (TUE)", 0, 3, 1)

# Fitur kategorikal
gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
family_history = st.selectbox("Riwayat Keluarga Obesitas", ["Yes", "No"])
favc = st.selectbox("Sering Konsumsi Makanan Tinggi Kalori?", ["Yes", "No"])
caec = st.selectbox("Konsumsi Camilan?", ["No", "Sometimes", "Frequently", "Always"])
smoke = st.selectbox("Merokok?", ["Yes", "No"])
scc = st.selectbox("Kendalikan Kalori?", ["Yes", "No"])
calc = st.selectbox("Konsumsi Alkohol?", ["No", "Sometimes", "Frequently"])
mtrans = st.selectbox("Transportasi", ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"])

# Encode kategorikal manual (harus sama dengan label encoder kamu saat training)
def encode(val, mapping):
    return mapping.get(val, 0)

gender_map = {"Male": 1, "Female": 0}
family_map = {"Yes": 1, "No": 0}
favc_map = {"Yes": 1, "No": 0}
caec_map = {"No": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
smoke_map = {"Yes": 1, "No": 0}
scc_map = {"Yes": 1, "No": 0}
calc_map = {"No": 0, "Sometimes": 1, "Frequently": 2}
mtrans_map = {"Public_Transportation": 0, "Walking": 1, "Automobile": 2, "Motorbike": 3, "Bike": 4}

# Gabungkan input
data = np.array([[
    age,
    height,
    weight,
    fcvc,
    ncp,
    ch2o,
    faf,
    tue,
    encode(gender, gender_map),
    encode(family_history, family_map),
    encode(favc, favc_map),
    encode(caec, caec_map),
    encode(smoke, smoke_map),
    encode(scc, scc_map),
    encode(calc, calc_map),
    encode(mtrans, mtrans_map)
]])

# Tombol prediksi
if st.button("Prediksi"):
    data_scaled = scaler.transform(data)
    pred = model.predict(data_scaled)[0]
    
    klasifikasi = {
        0: "Berat Badan Kurang",
        1: "Berat Badan Normal",
        2: "Kelebihan Berat Badan Tingkat I",
        3: "Kelebihan Berat Badan Tingkat II",
        4: "Obesitas Tipe I",
        5: "Obesitas Tipe II",
        6: "Obesitas Tipe III"
    }
    st.success(f"Hasil Prediksi: **{klasifikasi[pred]}**")
