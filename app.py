import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- Load model dan tools ---
with open("ObesityDataSet.csv", "rb") as f:
    data = joblib.load(f)
    model = data['model']
    scaler = data['scaler']
    label_encoders = data['label_encoders']
    target_encoder = data['target_encoder']
    numeric_cols = data['numeric_cols']
    feature_names = data['feature_names']

# --- Konfigurasi halaman ---
st.set_page_config(page_title="Prediksi Obesitas", page_icon="🍽", layout="centered")

st.title("Prediksi Tingkat Obesitas")
st.markdown("Masukkan informasi Anda untuk memprediksi tingkat obesitas:")

# --- Fungsi bantu pilihan ---
def pilihan(label, options):
    return st.selectbox(label, options)

# --- Input dari user ---
age = st.number_input("Umur", min_value=10, max_value=80, value=25)
height = st.number_input("Tinggi (m)", min_value=1.4, max_value=2.1, value=1.70, step=0.01)
weight = st.number_input("Berat (kg)", min_value=30, max_value=200, value=70)
ncp = st.slider("Jumlah makan utama per hari (NCP)", 1, 6, 3)
ch2o = st.slider("Konsumsi air per hari (liter)", 1.0, 5.0, 2.0, 0.1)
faf = st.slider("Aktivitas fisik per minggu (FAF)", 0, 14, 3)
tue = st.slider("Waktu pakai gadget per hari (TUE)", 0, 16, 4)
fcvc = st.slider("Frekuensi makan sayur per minggu (FCVC)", 0, 21, 5)

gender = pilihan("Jenis Kelamin", ["Male", "Female"])
calc = pilihan("Konsumsi kalori (CALC)", ["no", "Sometimes", "Frequently", "Always"])
favc = pilihan("Sering makan tinggi kalori (FAVC)", ["yes", "no"])
scc = pilihan("Minum soda (SCC)", ["yes", "no"])
smoke = pilihan("Merokok (SMOKE)", ["yes", "no"])
family = pilihan("Riwayat obesitas keluarga", ["yes", "no"])
caec = pilihan("Konsumsi alkohol (CAEC)", ["no", "Sometimes", "Frequently", "Always"])
mtrans = pilihan("Transportasi utama (MTRANS)", ["Public_Transportation", "Walking", "Bike", "Motorbike", "Automobile"])

# --- Persiapkan data untuk prediksi ---
input_dict = {
    "Age": age,
    "Height": height,
    "Weight": weight,
    "NCP": ncp,
    "CH2O": ch2o,
    "FAF": faf,
    "TUE": tue,
    "FCVC": fcvc,
    "Gender": gender,
    "CALC": calc,
    "FAVC": favc,
    "SCC": scc,
    "SMOKE": smoke,
    "family_history_with_overweight": family,
    "CAEC": caec,
    "MTRANS": mtrans
}

# Encode kategori
for col, le in label_encoders.items():
    input_dict[col] = le.transform([input_dict[col]])[0]

# Buat DataFrame
input_df = pd.DataFrame([input_dict])
input_df = input_df.reindex(columns=feature_names)
input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

# --- Prediksi ---
if st.button("Prediksi"):
    pred_encoded = model.predict(input_df)[0]
    pred_label = target_encoder.inverse_transform([pred_encoded])[0]
    pred_proba = model.predict_proba(input_df)[0]

    st.success(f"Tingkat obesitas Anda diprediksi: **{pred_label}**")
    
    st.markdown("### Probabilitas Semua Kelas:")
    proba_df = pd.DataFrame({
        "Tingkat Obesitas": target_encoder.inverse_transform(np.arange(len(pred_proba))),
        "Probabilitas": pred_proba
    }).sort_values("Probabilitas", ascending=False)

    st.dataframe(proba_df.style.format({"Probabilitas": "{:.2%}"}))
