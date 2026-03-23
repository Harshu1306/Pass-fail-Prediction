import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("student_pass_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Student Results")


midterm = st.number_input("Enter Your Score")


if st.button("Predict"):
    data = np.array([[midterm]])
    data = scaler.transform(data)
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Student Will Pass")
    else:
        st.error("Student Will Fail")