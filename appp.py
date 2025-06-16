import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# **Judul Aplikasi**
st.title("Prediksi Tingkat Obesitas")

# **Input Data**
st.header("Masukkan Data Diri dan Kebiasaan Anda")
umur = st.number_input("Umur (tahun)", min_value=0, max_value=120, value=30)
tinggi_badan = st.number_input("Tinggi badan (cm)", min_value=0, max_value=300, value=170)
berat_badan = st.number_input("Berat badan (kg)", min_value=0, max_value=500, value=70)
jumlah_makanan = st.number_input("Jumlah makanan utama per hari (NCP)", min_value=0, max_value=20, value=3)

# **Mempersiapkan Data untuk Model**
data = {
    "umur": [umur],
    "tinggi_badan": [tinggi_badan],
    "berat_badan": [berat_badan],
    "jumlah_makanan": [jumlah_makanan]
}
data_df = pd.DataFrame(data)

# **Model Dummy (Anda harus mengganti dengan model yang sebenarnya)**
# Misalkan kita sudah melatih model sebelumnya
# model = LogisticRegression()
# model.fit(X_train, y_train) # Ganti dengan data pelatihan Anda yang sebenarnya

# Prediksi (ganti dengan pemodelan yang sesuai)
def prediksi(data):
    # Model dummy: semua input dikembalikan sebagai obesitas rendah
    # Pada kenyataannya, Anda akan mengimplementasikan model yang sudah terlatih
    return "Obesitas Rendah"  # Ganti dengan logika prediksi yang sesuai
    
if st.button("Prediksi"):
    hasil = prediksi(data_df)
    st.success(f"Tingkat obesitas Anda diprediksi: {hasil}")

