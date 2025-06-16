import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Prediksi Tingkat Obesitas",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for styling (dark theme)
st.markdown(
    """
    <style>
    body {
        background-color: #222222;
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }
    .main {
        max-width: 800px;
        margin: 2rem auto;
        padding: 2rem 3rem;
        border-radius: 12px;
        box-shadow: rgba(0, 0, 0, 0.2) 0px 4px 12px;
    }
    h1 {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #FFFFFF;
        text-align: center;
    }
    h2 {
        font-size: 24px;
        font-weight: 600;
        margin-top: 1.5rem;
        color: #FFFFFF;
    }
    label {
        font-weight: 600;
        font-size: 16px;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4a90e2;
        color: white;
        padding: 12px 28px;
        font-size: 18px;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #357ab8;
        cursor: pointer;
    }
    .result {
        background-color: #3A3A3A;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        box-shadow: rgba(0, 0, 0, 0.2) 0px 4px 12px;
    }
    .caption {
        font-size: 14px;
        color: #CCCCCC;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main content
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("Prediksi Tingkat Obesitas")
st.write(
    "Masukkan data diri dan kebiasaan Anda dengan lengkap untuk memprediksi tingkat obesitas berdasarkan model terpercaya."
)

st.subheader("Informasi Pribadi dan Kebiasaan")

# Function to create selection boxes with explanations
def pilihan(label, options, penjelasan):
    st.write(f"**{label}**")
    for i, p in enumerate(penjelasan):
        st.caption(f"- {options[i]}: {p}")
    return st.selectbox(f"Pilih {label.lower()} Anda:", options)

# Options and descriptions for user input
# Your options and descriptions here...

# User input fields
# Your input fields here...

# Collecting user choices
# Your user choices here...

# Mapping categorical inputs to numerical values
# Your mapping code here...

# Prepare input data for prediction
# Your input data preparation code here...

@st.cache_data(show_spinner=False)
def load_and_train_model():
    df = pd.read_csv('ObesityDataSet.csv')

    # Clean the dataset
    # Your cleaning code here...

    return model, target_le, scaler, numeric_cols, feature_names

# Load and train the model
# Your loading and training code here...

# Validate and reorder input DataFrame columns
# Your validation and reordering code here...

# Scale the input data
# Your scaling code here...

# Prediction button
if st.button("Prediksi Tingkat Obesitas"):
    # Your prediction handling code here...

st.markdown("</div>", unsafe_allow_html=True)
