import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

st.set_page_config(
    page_title="Prediksi Tingkat Obesitas",
    page_icon=":bar_chart:",
)

st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data diri dan kebiasaan Anda.")

# Input fields for user data
age = st.number_input("Umur (tahun)", min_value=10, max_value=80, value=30, step=1)
height = st.number_input("Tinggi badan (cm)", min_value=140, max_value=210, value=170, step=1)
weight = st.number_input("Berat badan (kg)", min_value=30, max_value=200, value=70, step=1)
ncp = st.number_input("Jumlah makanan per hari (NCP)", min_value=1, max_value=6, value=3)
ch2o = st.number_input("Konsumsi air per hari (liter) (CH2O)", 1.0, 5.0, value=2.0, step=0.1)
faf = st.number_input("Frekuensi aktivitas fisik per minggu (FAF)", 0, 20, value=3)

gender = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
calc = st.selectbox("Konsumsi makanan tinggi kalori", ["Tidak pernah", "Kadang-kadang", "Sering", "Selalu"])

mapping = {
    "Perempuan": 0, "Laki-laki": 1,
    "Tidak pernah": 0, "Kadang-kadang": 1, "Sering": 2, "Selalu": 3
}

input_data = {
    "Age": age,
    "Height": height,
    "Weight": weight,
    "NCP": ncp,
    "CH2O": ch2o,
    "FAF": faf,
    "Gender": mapping[gender],
    "CALC": mapping[calc]
}

input_df = pd.DataFrame([input_data])

@st.cache_data
def load_and_train_model():
    df = pd.read_csv('ObesityDataSet.csv').dropna()
    le = LabelEncoder()
    df['Gender'] = le.fit_transform(df['Gender'])
    severity = le.fit_transform(df['NObeyesdad'])
    X = df.drop('NObeyesdad', axis=1)
    y = severity
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    model = RandomForestClassifier().fit(X, y)
    return model, scaler

model, scaler = load_and_train_model()
input_scaled = scaler.transform(input_df)

if st.button("Prediksi Tingkat Obesitas"):
    pred = model.predict(input_scaled)[0]
    st.success(f"Tingkat obesitas Anda diprediksi adalah: **{pred}**")

