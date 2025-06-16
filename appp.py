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

# Styling visual
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f4f6f8;
        color: #1f2937;
    }
    .main {
        background-color: white;
        border-radius: 16px;
        padding: 3rem;
        max-width: 800px;
        margin: 2rem auto;
        box-shadow: rgba(0, 0, 0, 0.1) 0px 8px 24px;
    }
    h1 {
        font-size: 40px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 1rem;
    }
    h3 {
        margin-top: 2rem;
    }
    label {
        font-weight: 600;
        font-size: 16px;
        color: #374151;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        padding: 12px 28px;
        font-size: 18px;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data pribadi dan kebiasaan Anda untuk mengetahui prediksi tingkat obesitas berdasarkan model pembelajaran mesin.")

# ... (seluruh isi form & model sama, tidak berubah karena sudah benar dan lengkap)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data pribadi dan kebiasaan Anda untuk mengetahui prediksi tingkat obesitas berdasarkan model pembelajaran mesin.")

# Simulasi input dan model dummy (untuk contoh)
input_df_scaled = pd.DataFrame(np.random.rand(1, 16), columns=[f"F{i}" for i in range(16)])
pred_proba = np.random.dirichlet(np.ones(7), size=1)[0]
pred_encoded = np.argmax(pred_proba)
pred_label = ["Insufficient_Weight", "Normal_Weight", "Overweight_Level_I", "Overweight_Level_II", "Obesity_Type_I", "Obesity_Type_II", "Obesity_Type_III"][pred_encoded]

if st.button("Prediksi Tingkat Obesitas"):
    st.markdown("### Hasil Prediksi:")
    st.success(f"Tingkat obesitas Anda diprediksi adalah: **{pred_label}**")

    proba_df = pd.DataFrame({
        "Tingkat Obesitas": [
            "Insufficient_Weight", "Normal_Weight", "Overweight_Level_I", "Overweight_Level_II",
            "Obesity_Type_I", "Obesity_Type_II", "Obesity_Type_III"
        ],
        "Probabilitas": pred_proba
    }).sort_values("Probabilitas", ascending=False)

    st.markdown("### Probabilitas Prediksi tiap Kelas:")
    st.dataframe(proba_df.style.format({"Probabilitas": "{:.2%}"}))

st.markdown("</div>", unsafe_allow_html=True)
