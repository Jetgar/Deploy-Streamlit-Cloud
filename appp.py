import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model_obesitas.pkl")

# Judul aplikasi
st.title("Prediksi Kategori Obesitas")

# Deskripsi
st.write("Isi data berikut untuk memprediksi kategori obesitas berdasarkan data Anda.")

# Form input
with st.form("input_form"):
    Gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
    Age = st.slider("Umur", 10, 100, 25)
    Height = st.number_input("Tinggi (meter)", min_value=1.0, max_value=2.5, value=1.7)
    Weight = st.number_input("Berat (kg)", min_value=20.0, max_value=200.0, value=65.0)
    family_history_with_overweight = st.selectbox("Riwayat keluarga overweight?", ["yes", "no"])
    FAVC = st.selectbox("Sering konsumsi makanan tinggi kalori (FAVC)?", ["yes", "no"])
    FCVC = st.slider("Frekuensi konsumsi sayur (0-3)", 0.0, 3.0, 2.0)
    NCP = st.slider("Jumlah makan utama per hari (1-4)", 1.0, 4.0, 3.0)
    CAEC = st.selectbox("Makan berlebih?", ["no", "Sometimes", "Frequently", "Always"])
    SMOKE = st.selectbox("Merokok?", ["yes", "no"])
    CH2O = st.slider("Asupan air (liter/hari)", 0.0, 3.0, 1.0)
    SCC = st.selectbox("Monitoring kalori?", ["yes", "no"])
    FAF = st.slider("Frekuensi aktivitas fisik (0-3)", 0.0, 3.0, 1.0)
    TUE = st.slider("Waktu depan komputer/gadget (0-3)", 0.0, 3.0, 1.0)
    CALC = st.selectbox("Konsumsi alkohol?", ["no", "Sometimes", "Frequently", "Always"])
    MTRANS = st.selectbox("Transportasi harian", ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"])

    submitted = st.form_submit_button("Prediksi")

# Proses prediksi
if submitted:
    input_data = pd.DataFrame([{
        "Gender": Gender,
        "Age": Age,
        "Height": Height,
        "Weight": Weight,
        "family_history_with_overweight": family_history_with_overweight,
        "FAVC": FAVC,
        "FCVC": FCVC,
        "NCP": NCP,
        "CAEC": CAEC,
        "SMOKE": SMOKE,
        "CH2O": CH2O,
        "SCC": SCC,
        "FAF": FAF,
        "TUE": TUE,
        "CALC": CALC,
        "MTRANS": MTRANS
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"✅ Prediksi kategori obesitas Anda: **{prediction}**")
