import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Tingkat Obesitas",
    page_icon=":bar_chart:",
    layout="centered"
)

# Styling CSS
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
    }
    header, footer {visibility: hidden;}
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

# Mulai konten utama
st.markdown('<div class="main">', unsafe_allow_html=True)

st.title("Prediksi Tingkat Obesitas")
st.write("Masukkan data diri dan kebiasaan Anda dengan lengkap untuk memprediksi tingkat obesitas berdasarkan model terpercaya.")
st.subheader("Informasi Pribadi dan Kebiasaan")

def pilihan(label, options, penjelasan):
    st.write(f"**{label}**")
    for i, p in enumerate(penjelasan):
        st.caption(f"- {options[i]}: {p}")
    return st.selectbox(f"Pilih {label.lower()} Anda:", options)

# Opsi dan deskripsi
gender_opts = ["Perempuan", "Laki-laki"]
gender_desc = ["Jenis kelamin wanita", "Jenis kelamin pria"]
calc_opts = ["Tidak pernah", "Kadang-kadang", "Sering", "Selalu"]
calc_desc = ["Tidak pernah mengonsumsi makanan tinggi kalori", "Kadang-kadang", "Sering", "Selalu"]
favc_opts = ["Tidak", "Ya"]
favc_desc = ["Tidak rutin konsumsi makanan tinggi kalori", "Rutin konsumsi"]
scc_opts = ["Tidak", "Ya"]
scc_desc = ["Tidak konsumsi minuman manis", "Konsumsi minuman manis"]
smoke_opts = ["Tidak", "Ya"]
smoke_desc = ["Tidak merokok", "Merokok"]
family_history_opts = ["Tidak", "Ya"]
family_history_desc = ["Tidak ada riwayat keluarga", "Ada riwayat keluarga"]
caec_opts = ["Tidak pernah", "Kadang-kadang", "Sering", "Selalu"]
caec_desc = ["Tidak konsumsi alkohol", "Kadang-kadang", "Sering", "Selalu"]
mtrans_opts = ["Mobil pribadi", "Motor", "Transportasi umum", "Berjalan kaki", "Sepeda"]
mtrans_desc = ["Mobil", "Motor", "Umum", "Jalan kaki", "Sepeda"]

# Input numerik
age = st.number_input("Umur (tahun)", min_value=10, max_value=80, value=30)
height = st.number_input("Tinggi badan (cm)", min_value=140, max_value=210, value=170)
weight = st.number_input("Berat badan (kg)", min_value=30, max_value=200, value=70)
ncp = st.number_input("Jumlah makanan utama per hari (NCP)", min_value=1, max_value=6, value=3)
ch2o = st.number_input("Konsumsi air per hari (liter) (CH2O)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)
faf = st.number_input("Frekuensi aktivitas fisik/minggu (FAF)", min_value=0, max_value=20, value=3)
tue = st.number_input("Waktu pakai gadget per hari (jam) (TUE)", min_value=0, max_value=16, value=4)
fcvc = st.number_input("Frekuensi konsumsi sayur/minggu (FCVC)", min_value=0, max_value=21, value=3)

# Input kategorik
gender = pilihan("Jenis Kelamin (Gender)", gender_opts, gender_desc)
calc = pilihan("Konsumsi makanan tinggi kalori (CALC)", calc_opts, calc_desc)
favc = pilihan("Mengonsumsi makanan tinggi kalori secara rutin (FAVC)", favc_opts, favc_desc)
scc = pilihan("Konsumsi minuman manis (SCC)", scc_opts, scc_desc)
smoke = pilihan("Merokok (SMOKE)", smoke_opts, smoke_desc)
family_history = pilihan("Riwayat keluarga obesitas", family_history_opts, family_history_desc)
caec = pilihan("Konsumsi alkohol (CAEC)", caec_opts, caec_desc)
mtrans = pilihan("Moda transportasi utama (MTRANS)", mtrans_opts, mtrans_desc)

# Mapping input ke angka
mapping = {
    "Gender": {"Perempuan": 0, "Laki-laki": 1},
    "CALC": {"Tidak pernah": 0, "Kadang-kadang": 1, "Sering": 2, "Selalu": 3},
    "FAVC": {"Tidak": 0, "Ya": 1},
    "SCC": {"Tidak": 0, "Ya": 1},
    "SMOKE": {"Tidak": 0, "Ya": 1},
    "family_history_with_overweight": {"Tidak": 0, "Ya": 1},
    "CAEC": {"Tidak pernah": 0, "Kadang-kadang": 1, "Sering": 2, "Selalu": 3},
    "MTRANS": {"Mobil pribadi": 0, "Motor": 1, "Transportasi umum": 2, "Berjalan kaki": 3, "Sepeda": 4}
}

# Dataframe input
input_data = {
    "Age": age,
    "Height": height,
    "Weight": weight,
    "NCP": ncp,
    "CH2O": ch2o,
    "FAF": faf,
    "TUE": tue,
    "FCVC": fcvc,
    "Gender": mapping["Gender"][gender],
    "CALC": mapping["CALC"][calc],
    "FAVC": mapping["FAVC"][favc],
    "SCC": mapping["SCC"][scc],
    "SMOKE": mapping["SMOKE"][smoke],
    "family_history_with_overweight": mapping["family_history_with_overweight"][family_history],
    "CAEC": mapping["CAEC"][caec],
    "MTRANS": mapping["MTRANS"][mtrans]
}

input_df = pd.DataFrame([input_data])

@st.cache_data(show_spinner=False)
def load_and_train_model():
    df = pd.read_csv('ObesityDataSet.csv')

    # Bersihkan data
    cols_clean = ['Gender', 'CALC', 'FAVC', 'SCC', 'SMOKE', 'family_history_with_overweight', 'CAEC', 'MTRANS']
    df = df[~df[cols_clean].isin(['?']).any(axis=1)].copy()
    df.dropna(inplace=True)

    # Label encode kategorik
    target = 'NObeyesdad'
    label_encoders = {}
    for col in df.select_dtypes(include='object'):
        if col != target:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

    target_le = LabelEncoder()
    df[target] = target_le.fit_transform(df[target])

    # Split X dan y
    X = df.drop(target, axis=1)
    y = df[target]

    # Scaling numerik
    numeric_cols = ['Age', 'Height', 'Weight', 'NCP', 'CH2O', 'FAF', 'TUE', 'FCVC']
    scaler = StandardScaler()
    X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model, target_le, scaler, numeric_cols, list(X.columns)

model, target_le, scaler, numeric_cols, feature_names = load_and_train_model()

# Persiapkan input sesuai model
input_df = input_df.reindex(columns=feature_names)
input_df_scaled = input_df.copy()
input_df_scaled[numeric_cols] = scaler.transform(input_df[numeric_cols])

# Prediksi
if st.button("Prediksi Tingkat Obesitas"):
    pred = model.predict(input_df_scaled)[0]
    label = target_le.inverse_transform([pred])[0]
    proba = model.predict_proba(input_df_scaled)[0]

    st.markdown("### Hasil Prediksi:")
    st.success(f"Tingkat obesitas Anda diprediksi adalah: **{label}**")

    # Tampilkan probabilitas semua kelas
    proba_df = pd.DataFrame({
        "Tingkat Obesitas": target_le.inverse_transform(np.arange(len(proba))),
        "Probabilitas": proba
    }).sort_values("Probabilitas", ascending=False)

    st.markdown("### Probabilitas Tiap Kategori:")
    st.dataframe(proba_df.style.format({"Probabilitas": "{:.2%}"}))

st.markdown("</div>", unsafe_allow_html=True)
