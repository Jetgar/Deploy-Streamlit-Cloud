import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

# --- Konfigurasi halaman ---
st.set_page_config(
    page_title="Prediksi Tingkat Obesitas",
    page_icon=":bar_chart:",
    layout="centered",
    initial_sidebar_state="auto",
)

# --- Styling CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
        color: #1f2937;
        font-family: 'Inter', sans-serif;
        max-width: 700px;
        margin: 2rem auto;
        padding: 2rem 3rem;
        border-radius: 12px;
        box-shadow: rgba(0,0,0,0.08) 0px 8px 24px;
    }
    h1 {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #111827;
    }
    label {
        font-weight: 600;
        font-size: 16px;
        color: #374151;
    }
    .stButton>button {
        background-color: #111827;
        color: white;
        padding: 12px 28px;
        font-size: 18px;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# --- Judul aplikasi ---
st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data diri dan kebiasaan Anda dengan lengkap untuk memprediksi tingkat obesitas berdasarkan model terpercaya.")

# --- Awal div utama untuk styling ---
st.markdown('<div class="main">', unsafe_allow_html=True)

# --- Fungsi pilihan dengan deskripsi ---
def pilihan(label, options, penjelasan):
    st.write(f"**{label}**")
    for i, p in enumerate(penjelasan):
        st.caption(f"- {options[i]}: {p}")
    return st.selectbox(f"Pilih {label.lower()} Anda:", options)

# --- Daftar pilihan ---
gender_opts = ["Perempuan", "Laki-laki"]
gender_desc = ["Jenis kelamin wanita", "Jenis kelamin pria"]

calc_opts = ["Tidak pernah", "Kadang-kadang", "Sering", "Selalu"]
calc_desc = [
    "Tidak pernah mengonsumsi makanan tinggi kalori",
    "Kadang-kadang mengonsumsi makanan tinggi kalori",
    "Sering mengonsumsi makanan tinggi kalori",
    "Selalu mengonsumsi makanan tinggi kalori"
]

favc_opts = ["Tidak", "Ya"]
favc_desc = ["Tidak mengonsumsi makanan tinggi kalori secara rutin", "Mengonsumsi makanan tinggi kalori secara rutin"]

scc_opts = ["Tidak", "Ya"]
scc_desc = ["Tidak mengonsumsi minuman bersoda atau manis", "Mengonsumsi minuman bersoda atau manis"]

smoke_opts = ["Tidak", "Ya"]
smoke_desc = ["Tidak merokok", "Merokok"]

family_history_opts = ["Tidak", "Ya"]
family_history_desc = ["Tidak ada riwayat obesitas di keluarga", "Ada riwayat obesitas di keluarga"]

caec_opts = ["Tidak pernah", "Kadang-kadang", "Sering", "Selalu"]
caec_desc = ["Tidak mengonsumsi alkohol", "Kadang-kadang mengonsumsi alkohol", "Sering", "Selalu"]

mtrans_opts = ["Mobil pribadi", "Motor", "Transportasi umum", "Berjalan kaki", "Sepeda"]
mtrans_desc = ["Mobil", "Motor", "Transportasi umum", "Berjalan kaki", "Sepeda"]

# --- Input numerik ---
age = st.number_input("Umur (tahun)", min_value=10, max_value=80, value=30)
height = st.number_input("Tinggi badan (cm)", min_value=140, max_value=210, value=170)
weight = st.number_input("Berat badan (kg)", min_value=30, max_value=200, value=70)
ncp = st.number_input("Jumlah makanan utama per hari (NCP)", 1, 6, 3)
ch2o = st.number_input("Konsumsi air per hari (liter)", 1.0, 5.0, 2.0, step=0.1)
faf = st.number_input("Frekuensi aktivitas fisik per minggu", 0, 20, 3)
tue = st.number_input("Waktu menggunakan gadget per hari (jam)", 0, 16, 4)
fcvc = st.number_input("Frekuensi konsumsi sayur per minggu", 0, 21, 3)

# --- Input pilihan ---
gender = pilihan("Jenis Kelamin", gender_opts, gender_desc)
calc = pilihan("Konsumsi makanan tinggi kalori", calc_opts, calc_desc)
favc = pilihan("Makanan tinggi kalori rutin", favc_opts, favc_desc)
scc = pilihan("Minuman manis / soda", scc_opts, scc_desc)
smoke = pilihan("Merokok", smoke_opts, smoke_desc)
family = pilihan("Riwayat obesitas keluarga", family_history_opts, family_history_desc)
caec = pilihan("Konsumsi alkohol", caec_opts, caec_desc)
mtrans = pilihan("Moda transportasi", mtrans_opts, mtrans_desc)

# --- Konversi input ke format model ---
mapping = {
    "Gender": {"Perempuan": 0, "Laki-laki": 1},
    "CALC": {"Tidak pernah": 0, "Kadang-kadang": 1, "Sering": 2, "Selalu": 3},
    "FAVC": {"Tidak": 0, "Ya": 1},
    "SCC": {"Tidak": 0, "Ya": 1},
    "SMOKE": {"Tidak": 0, "Ya": 1},
    "family_history_with_overweight": {"Tidak": 0, "Ya": 1},
    "CAEC": {"Tidak pernah": 0, "Kadang-kadang": 1, "Sering": 2, "Selalu": 3},
    "MTRANS": {
        "Mobil pribadi": 0, "Motor": 1, "Transportasi umum": 2,
        "Berjalan kaki": 3, "Sepeda": 4
    }
}

input_data = {
    "Age": age, "Height": height, "Weight": weight, "NCP": ncp,
    "CH2O": ch2o, "FAF": faf, "TUE": tue, "FCVC": fcvc,
    "Gender": mapping["Gender"][gender],
    "CALC": mapping["CALC"][calc],
    "FAVC": mapping["FAVC"][favc],
    "SCC": mapping["SCC"][scc],
    "SMOKE": mapping["SMOKE"][smoke],
    "family_history_with_overweight": mapping["family_history_with_overweight"][family],
    "CAEC": mapping["CAEC"][caec],
    "MTRANS": mapping["MTRANS"][mtrans]
}

input_df = pd.DataFrame([input_data])

# --- Load model dan scaler ---
@st.cache_data(show_spinner=False)
def load_model():
    df = pd.read_csv("ObesityDataSet.csv")
    df.replace("?", np.nan, inplace=True)
    df.dropna(inplace=True)

    num_cols = ['Age', 'Height', 'Weight', 'NCP', 'CH2O', 'FAF', 'TUE', 'FCVC']
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.dropna(inplace=True)
    label_encoders = {}
    for col in df.select_dtypes(include='object'):
        if col != "NObeyesdad":
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

    target_le = LabelEncoder()
    df["NObeyesdad"] = target_le.fit_transform(df["NObeyesdad"])

    X = df.drop("NObeyesdad", axis=1)
    y = df["NObeyesdad"]

    scaler = StandardScaler()
    X[num_cols] = scaler.fit_transform(X[num_cols])

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model, scaler, target_le, num_cols, X.columns.tolist()

model, scaler, target_le, num_cols, feature_order = load_model()

# --- Transformasi dan prediksi ---
input_df = input_df.reindex(columns=feature_order)
input_df[num_cols] = scaler.transform(input_df[num_cols])

if st.button("Prediksi Tingkat Obesitas"):
    pred_encoded = model.predict(input_df)[0]
    pred_label = target_le.inverse_transform([pred_encoded])[0]
    proba = model.predict_proba(input_df)[0]

    st.success(f"Tingkat obesitas Anda diprediksi: **{pred_label}**")

    st.markdown("### Probabilitas Semua Kelas:")
    prob_df = pd.DataFrame({
        "Kategori": target_le.inverse_transform(np.arange(len(proba))),
        "Probabilitas": proba
    }).sort_values("Probabilitas", ascending=False)

    st.dataframe(prob_df.style.format({"Probabilitas": "{:.2%}"}))

# --- Tutup div styling utama ---
st.markdown('</div>', unsafe_allow_html=True)

