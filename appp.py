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
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
        color: #1e293b;
    }
    .main {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 3rem;
        max-width: 900px;
        margin: 2rem auto;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    h1 {
        font-size: 44px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 1.2rem;
        text-align: center;
    }
    h3 {
        margin-top: 2.5rem;
        font-size: 24px;
        color: #0f172a;
    }
    label {
        font-weight: 600;
        font-size: 16px;
        color: #374151;
    }
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6, #06b6d4);
        color: white;
        padding: 14px 30px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2563eb, #0891b2);
        transform: scale(1.02);
        cursor: pointer;
    }
    .stDataFrame th {
        background-color: #e0f2fe !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data pribadi dan kebiasaan Anda untuk mengetahui prediksi tingkat obesitas berdasarkan model pembelajaran mesin.")

# Simulasi input dan model dummy (untuk contoh)
input_df_scaled = pd.DataFrame(np.random.rand(1, 16), columns=[f"F{i}" for i in range(16)])
pred_proba = np.random.dirichlet(np.ones(7), size=1)[0]
pred_encoded = np.argmax(pred_proba)
pred_label = [
    "Insufficient_Weight", "Normal_Weight", "Overweight_Level_I",
    "Overweight_Level_II", "Obesity_Type_I", "Obesity_Type_II", "Obesity_Type_III"
][pred_encoded]

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

