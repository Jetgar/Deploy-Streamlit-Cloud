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
        font-family: 'Inter', sans-serif;
        background: linear-gradient(to right, #f0f4f8, #d9e2ec);
        color: #1f2937;
    }
    .main {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 2.5rem 3rem;
        max-width: 860px;
        margin: 2rem auto;
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.1);
    }
    h1 {
        font-size: 44px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    h3 {
        margin-top: 2rem;
        font-size: 22px;
        color: #1e293b;
    }
    label, .stTextInput>div>label, .stNumberInput>div>label {
        font-weight: 600;
        font-size: 16px;
        color: #334155;
    }
    .stButton>button {
        background: linear-gradient(to right, #111827, #2563eb);
        color: #ffffff;
        padding: 12px 28px;
        font-size: 17px;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #2563eb, #111827);
        transform: translateY(-1px);
        cursor: pointer;
    }
    .stDataFrame th {
        background-color: #f0f9ff !important;
    }
    .stDataFrame td {
        font-size: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data pribadi dan kebiasaan Anda untuk mengetahui prediksi tingkat obesitas berdasarkan model pembelajaran mesin.")

# Placeholder data and dummy prediction for visual presentation
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
