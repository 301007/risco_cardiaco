

import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo salvo
modelo = joblib.load('modelo_risco_cardiaco.joblib')

# Título
st.title("Predição de Risco Cardíaco")
st.markdown("Preencha os dados do paciente para verificar o risco de ataque cardíaco.")

# Entradas do usuário
age = st.number_input("Idade", min_value=1, max_value=120, value=50)
gender = st.selectbox("Gênero", ["Masculino", "Feminino"])
heart_rate = st.number_input("Frequência Cardíaca (bpm)", min_value=30, max_value=200, value=80)
systolic = st.number_input("Pressão Sistólica (mmHg)", min_value=80, max_value=250, value=120)
diastolic = st.number_input("Pressão Diastólica (mmHg)", min_value=40, max_value=150, value=80)
blood_sugar = st.number_input("Glicose no sangue (mg/dL)", min_value=50, max_value=500, value=100)
ck_mb = st.number_input("CK-MB (U/L)", min_value=0.0, max_value=100.0, value=25.0)
troponin = st.number_input("Troponina (ng/mL)", min_value=0.0, max_value=50.0, value=0.05)

# Botão de previsão
if st.button("Prever Risco"):
    # Prepara os dados de entrada
    dados = pd.DataFrame({
        'Age': [age],
        'Gender': [1 if gender == "Masculino" else 0],
        'Heart rate': [heart_rate],
        'Systolic blood pressure': [systolic],
        'Diastolic blood pressure': [diastolic],
        'Blood sugar': [blood_sugar],
        'CK-MB': [ck_mb],
        'Troponin': [troponin]
    })

    # Fazer a previsão
    predicao = modelo.predict(dados)[0]
    prob = modelo.predict_proba(dados)[0][1]

    # Mostrar resultado
    if predicao == 1:
        st.error(f"⚠️ Alto risco de ataque cardíaco (probabilidade: {prob:.1%})")
    else:
        st.success(f"✅ Baixo risco de ataque cardíaco (probabilidade: {prob:.1%})")
