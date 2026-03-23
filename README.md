# Pass-Fail Prediction using Machine Learning

## Project Overview
This project predicts whether a student will pass or fail based on academic performance indicators such as attendance, homework score, midterm marks, and study hours. The model is built using Machine Learning and deployed using a Streamlit web application for user interaction.

---

## Problem Statement
The goal of this project is to predict student performance (Pass/Fail) using academic-related features. This can help identify student performance patterns and assist in academic monitoring.

---

## Dataset Features
The model uses the following input features:

- Attendance
- Homework Score
- Midterm Score
- Study Hours

Output:
- Pass → 1
- Fail → 0

---

## Machine Learning Workflow
The following steps were performed in this project:

1. Data Loading
2. Feature Selection
3. Train-Test Split (80% Training, 20% Testing)
4. Feature Scaling using StandardScaler
5. Model Training using Logistic Regression
6. Model Evaluation using Accuracy and Confusion Matrix
7. Model Saving using Pickle
8. Deployment using Streamlit

---

## Model Used
- Logistic Regression (Scikit-learn)

---

## Model Performance
Model Accuracy: **1.0**

### Reason for High Accuracy
The model achieved very high accuracy because:
- The dataset is small
- The input features are strongly related to the final result
- The pass/fail outcome can be clearly separated based on the given features
- The model was able to correctly classify all test samples

Confusion Matrix:
[[8 0]
[0 12]]

Interpretation:
- 8 Fail predictions were correct
- 12 Pass predictions were correct
- No incorrect predictions

---

## Technologies Used
- Python
- NumPy
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- GitHub

---

## Project Structure
pass-fail-Prediction
│
├── app.py
├── student_pass_model.pkl
├── scaler.pkl
├── dataset.csv
├── requirements.txt
└── README.md

---

## Application Description
The Streamlit web application allows users to enter student academic details such as attendance, homework score, midterm marks, and study hours. Based on the input values, the machine learning model predicts whether the student will pass or fail.

---

## Future Improvements
- Use larger dataset
- Try different machine learning algorithms
- Perform hyperparameter tuning
- Deploy application online
- Add performance visualization
- Add probability prediction

---


