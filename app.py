import streamlit as st
import pickle
import numpy as np

st.title("Drug Prediction System")

with open("xgb_classifier.pkl","rb") as file:
    xgb_model = pickle.load(file)

def Predict_function(Age,Gender,Bp,Chelosterol,Na_to_K):
    input_array = np.array([[Age,Gender,Bp,Chelosterol,Na_to_K]])
    drug_prediction = xgb_model.predict(input_array)
    return drug_prediction

Age = st.slider("Age", min_value=1,max_value=100)
Gender = st.selectbox("Gender",["Male","Female"]) 
Bp = st.selectbox("Bp",["Low","Normal", "High"]) 
Chelosterol = st.selectbox("Chelosterol", ["Normal","High"])
Na_to_K = st.slider("Na_to_K", min_value=1,max_value=50)

Gender = 1 if Gender == "Male" else 0
bp_mapping = {"High":0,"Low":1,"Normal":2}
Bp = bp_mapping[Bp]
Chelosterol_mapping = {"High":0,"Normal":1}
Chelosterol = Chelosterol_mapping[Chelosterol]

if st.button("Predict"):
    st.write(f"user values are {Age,Gender,Bp,Chelosterol,Na_to_K}")
    prediction = Predict_function(Age,Gender,Bp,Chelosterol,Na_to_K)
    drug_dct = {0:"drugA",1:"drugB",2:"drugC",3:"drugX",4:"drugY"}
    st.write(f"\n The prediction is {drug_dct[prediction[0]]}")

