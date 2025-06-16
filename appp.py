import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

st.set_page_config(
    page_title="Prediksi Tingkat Obesitas",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for dark theme
st.markdown("""
    <style>
        .main {
            background-color: #1E1E1E;
            color: #FFFFFF;
            font-family: 'Inter', sans-serif;
            max-width: 700px;
            margin: 2rem auto;
            padding: 20px;
            border-radius: 12px;
            box-shadow: rgba(0, 0, 0, 0.1) 0px 8px 24px;
        }
        h1 {
            font-size: 36px;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #FFD700;
        }
        h2 {
            font-size: 24px;
            font-weight: 500;
            color: #FFD700;
        }
        label {
            font-weight: 600;
            font-size: 16px;
            color: #FFFFFF;
        }
        .stButton>button {
            background-color: #FFD700;
            color: #1E1E1E;
            padding: 12px 28px;
            font-size: 18px;
            font-weight: 700;
            border-radius: 8px;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #FFA500;
            cursor: pointer;
        }
        .stSelectbox, .stNumberInput {
            background-color: #2E2E2E;
            color: #FFFFFF;
            border: 1px solid #444444;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("Prediksi Tingkat Obesitas")
st.write(
    "Masukkan data diri dan kebiasaan Anda dengan lengkap untuk memprediksi tingkat obesitas berdasarkan model terpercaya."
)

st.subheader("Informasi Pribadi dan Kebiasaan")

def pilihan(label, options, penjelasan):
    st.write(f"**{label}**")
    for i, p in enumerate(penjelasan):
        st.caption(f"- {options[i]}: {p}")
    return st.selectbox(f"Pilih {label.lower()} Anda:", options)

# Options and descriptions
gender_opts = ["Perempuan", "Laki-laki"]
gender_desc = ["Jenis kelamin wanita", "Jenis kelamin pria"]

calc_opts = ["Tidak pernah", "Kadang-kadang", "Sering", "Selalu"]
calc_desc = [
    "Tidak pernah mengonsumsi makanan tinggi kalori",
    "Mengonsumsi makanan tinggi kalori kadang-kadang",
    "Sering mengonsumsi makanan tinggi kalori",
    "Selalu mengonsumsi makanan tinggi kalori"
]

# Other options...

# Input fields
age = st.number_input("Umur (tahun)", min_value=10, max_value=80, value=30, step=1)
height = st.number_input("Tinggi badan (cm)", min_value=140, max_value=210, value=170, step=1)
weight = st.number_input("Berat badan (kg)", min_value=30, max_value=200, value=70, step=1)
# ... more input fields ...

gender = pilihan("Jenis Kelamin (Gender)", gender_opts, gender_desc)
calc = pilihan("Konsumsi makanan tinggi kalori (CALC)", calc_opts, calc_desc)
# ... other `pilihan` calls ...

# Model loading and prediction code stays the same

if st.button("Prediksi Tingkat Obesitas"):
    # Prediction logic...
    st.markdown("### Hasil Prediksi:")
    st.success(f"Tingkat obesitas Anda diprediksi adalah: **{pred_label}**")
    # Display probabilities...

st.markdown("</div>", unsafe_allow_html=True)
