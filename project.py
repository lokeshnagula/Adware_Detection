import streamlit as st
import numpy as np
import pickle

# Load the trained model
model_path = "model.pkl"  # Replace with your actual model file
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Feature names
feature_names = [
    "Flow IAT Max", "URG Flag Count", "Idle Min", "Subflow Fwd Packets",
    "Fwd Packets/s", "Fwd IAT Min", "Subflow Bwd Bytes", "Init_Win_bytes_backward",
    "Flow IAT Std", "Fwd IAT Mean", "Max Packet Length", "Init_Win_bytes_forward",
    "Flow Duration", "Subflow Bwd Packets", "Active Std"
]

# Label mapping
label_map = {
    0: 'ADWARE_DOWGIN',
    1: 'ADWARE_EWIND',
    2: 'ADWARE_FEIWO',
    3: 'ADWARE_GOOLIGAN',
    4: 'ADWARE_KEMOGE',
    5: 'ADWARE_KOODOUS',
    6: 'ADWARE_MOBIDASH',
    7: 'ADWARE_SELFMITE',
    8: 'ADWARE_SHUANET',
    9: 'ADWARE_YOUMI'
}

# --- Dark Theme Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #121212;
            color: #ffffff;
            padding: 30px;
            border-radius: 10px;
        }
        .title {
            color: #00e676;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #888888;
            margin-top: 40px;
        }
        .stButton > button {
            background-color: #00e676;
            color: black;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1.5em;
        }
        label {
            color: #ffffff !important;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# --- Page Content ---
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🧠 Adware Attack Prediction</div>', unsafe_allow_html=True)
st.write("Please enter values for the following features:")

# Input Fields
input_data = []
cols = st.columns(3)
for idx, feature in enumerate(feature_names):
    with cols[idx % 3]:
        value = st.number_input(f"{feature}", min_value=0.0, step=0.01, key=feature)
        input_data.append(value)

input_array = np.array(input_data).reshape(1, -1)

# Predict Button
if st.button("🔮 Predict"):
    prediction_number = model.predict(input_array)[0]
    prediction_label = label_map.get(prediction_number, "Unknown Label")
    st.success(f"🎯 **Predicted Label:** `{prediction_label}` (Class {prediction_number})")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Developed with ❤️ using Streamlit | Dark Edition</div>', unsafe_allow_html=True)


