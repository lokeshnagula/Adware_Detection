# 🧠 Adware Attack Prediction App

A web-based machine learning application built using **Streamlit** that predicts the type of Android adware attack based on network traffic features. Designed with a sleek dark theme for a modern user experience.

## 🚀 Features

- 🔮 Predicts one of 10 types of Android adware attacks
- 📊 Takes 15 traffic-based input features
- 💡 Built with a trained machine learning model (`model.pkl`)
- 🖤 Fully styled with a custom dark theme
- 📦 Easy to deploy with `requirements.txt`

## 🧰 Tech Stack

- Python 🐍
- Streamlit
- NumPy
- Scikit-learn
- Pickle (for model serialization)

## 📋 Input Features

1. Flow IAT Max  
2. URG Flag Count  
3. Idle Min  
4. Subflow Fwd Packets  
5. Fwd Packets/s  
6. Fwd IAT Min  
7. Subflow Bwd Bytes  
8. Init_Win_bytes_backward  
9. Flow IAT Std  
10. Fwd IAT Mean  
11. Max Packet Length  
12. Init_Win_bytes_forward  
13. Flow Duration  
14. Subflow Bwd Packets  
15. Active Std  

## 🏷️ Output Labels

- ADWARE_DOWGIN  
- ADWARE_EWIND  
- ADWARE_FEIWO  
- ADWARE_GOOLIGAN  
- ADWARE_KEMOGE  
- ADWARE_KOODOUS  
- ADWARE_MOBIDASH  
- ADWARE_SELFMITE  
- ADWARE_SHUANET  
- ADWARE_YOUMI  

## 🔧 Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/adware-attack-predictor.git
   cd adware-attack-predictor
