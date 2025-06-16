import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Tingkat Obesitas",
    page_icon=":bar_chart:",
    layout="centered",
)

# Styling: menghilangkan kotak putih di atas
hide_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 2rem;
        }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Judul aplikasi
st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
st.title("🎯 Prediksi Tingkat Obesitas")
st.markdown("Masukkan data pribadi & kebiasaan Anda untuk memprediksi tingkat obesitas.")
st.markdown('</div>', unsafe_allow_html=True)

# Fungsi pilihan dengan penjelasan
def pilihan(label, options, penjelasan):
    st.write(f"**{label}**")
    for i, p in enumerate(penjelasan):
        st.caption(f"- {options[i]}: {p}")
    return st.selectbox(f"Pilih {label.lower()}:", options)

# Opsi dan deskripsi
gender_opts = ["Perempuan", "Laki-laki"]
gender_desc = ["Jenis kelamin wanita", "Jenis kelamin pria"]
calc_opts = ["Tidak pernah", "Kadang-kadang", "Sering", "Selalu"]
calc_desc = ["Tidak pernah makan tinggi kalori", "Kadang-kadang", "Sering", "Selalu"]
favc_opts = ["Tidak", "Ya"]
favc_desc = ["Tidak rutin makanan tinggi kalori", "Rutin"]
scc_opts = ["Tidak", "Ya"]
scc_desc = ["Tidak minuman manis", "Minuman manis"]
smoke_opts = ["Tidak", "Ya"]
smoke_desc = ["Tidak merokok", "Merokok"]
family_history_opts = ["Tidak", "Ya"]
family_history_desc = ["Tidak ada riwayat", "Ada riwayat kelebihan berat badan"]
caec_opts = ["Tidak pernah", "Kadang-kadang", "Sering", "Selalu"]
caec_desc = ["Tidak pernah minum alkohol", "Kadang", "Sering", "Selalu"]
mtrans_opts = ["Mobil pribadi", "Motor", "Transportasi umum", "Berjalan kaki", "Sepeda"]
mtrans_desc = mtrans_opts

# Input numerik
age = st.number_input("Umur (tahun)", 10, 80, 30)
height = st.number_input("Tinggi badan (cm)", 140, 210, 170)
weight = st.number_input("Berat badan (kg)", 30, 200, 70)
ncp = st.number_input("Jumlah makanan utama/hari", 1, 6, 3)
ch2o = st.number_input("Air minum per hari (liter)", 1.0, 5.0, 2.0, step=0.1)
faf = st.number_input("Aktivitas fisik/minggu (kali)", 0, 20, 3)
tue = st.number_input("Waktu layar per hari (jam)", 0, 16, 4)
fcvc = st.number_input("Frekuensi makan sayur/minggu", 0, 21, 3)

# Input kategori
gender = pilihan("Jenis Kelamin", gender_opts, gender_desc)
calc = pilihan("Konsumsi Kalori Tinggi", calc_opts, calc_desc)
favc = pilihan("Kebiasaan Kalori Tinggi", favc_opts, favc_desc)
scc = pilihan("Konsumsi Minuman Manis", scc_opts, scc_desc)
smoke = pilihan("Merokok", smoke_opts, smoke_desc)
family_history = pilihan("Riwayat Keluarga Overweight", family_history_opts, family_history_desc)
caec = pilihan("Konsumsi Alkohol", caec_opts, caec_desc)
mtrans = pilihan("Moda Transportasi", mtrans_opts, mtrans_desc)

# Mapping input
mappings = {
    "Gender": {"Perempuan": 0, "Laki-laki": 1},
    "CALC": dict(zip(calc_opts, range(4))),
    "FAVC": {"Tidak": 0, "Ya": 1},
    "SCC": {"Tidak": 0, "Ya": 1},
    "SMOKE": {"Tidak": 0, "Ya": 1},
    "family_history_with_overweight": {"Tidak": 0, "Ya": 1},
    "CAEC": dict(zip(caec_opts, range(4))),
    "MTRANS": dict(zip(mtrans_opts, range(5))),
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
    "Gender": mappings["Gender"][gender],
    "CALC": mappings["CALC"][calc],
    "FAVC": mappings["FAVC"][favc],
    "SCC": mappings["SCC"][scc],
    "SMOKE": mappings["SMOKE"][smoke],
    "family_history_with_overweight": mappings["family_history_with_overweight"][family_history],
    "CAEC": mappings["CAEC"][caec],
    "MTRANS": mappings["MTRANS"][mtrans],
}
input_df = pd.DataFrame([input_data])

# Fungsi load dan training model
@st.cache_data
def load_and_train_model():
    df = pd.read_csv("ObesityDataSet.csv")
    df = df[~df[['Gender', 'CALC', 'FAVC', 'SCC', 'SMOKE', 'family_history_with_overweight', 'CAEC', 'MTRANS']].isin(['?']).any(axis=1)].copy()
    df = df.dropna()
    num_cols = ['Age', 'Height', 'Weight', 'NCP', 'CH2O', 'FAF', 'TUE', 'FCVC']
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.dropna(inplace=True)

    le_dict = {}
    for col in df.select_dtypes(include='object').columns:
        if col != 'NObeyesdad':
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            le_dict[col] = le

    target_le = LabelEncoder()
    df["NObeyesdad"] = target_le.fit_transform(df["NObeyesdad"])

    X = df.drop("NObeyesdad", axis=1)
    y = df["NObeyesdad"]
    scaler = StandardScaler()
    X[num_cols] = scaler.fit_transform(X[num_cols])

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, target_le, scaler, num_cols, list(X.columns)

model, target_le, scaler, num_cols, feature_names = load_and_train_model()

input_df = input_df.reindex(columns=feature_names)
input_df[num_cols] = scaler.transform(input_df[num_cols])

# Tombol prediksi
if st.button("🔍 Prediksi Tingkat Obesitas"):
    pred = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]
    label = target_le.inverse_transform([pred])[0]
    st.success(f"Tingkat obesitas Anda diprediksi adalah: **{label}**")

    proba_df = pd.DataFrame({
        "Tingkat Obesitas": target_le.inverse_transform(np.arange(len(proba))),
        "Probabilitas": proba
    }).sort_values("Probabilitas", ascending=False)

    st.markdown("#### Rincian Probabilitas:")
    st.dataframe(proba_df.style.format({"Probabilitas": "{:.2%}"}))
