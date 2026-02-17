# 🏠 House Price Prediction using Machine Learning & Streamlit

## 📌 Project Overview
This project predicts house prices based on various features using a Machine Learning model.
The model was trained using Python and scikit-learn in Google Colab and deployed as an interactive
web application using Streamlit.

---

## 🧠 Problem Statement
To build a machine learning model that can accurately predict house prices based on
house characteristics such as area, number of bedrooms, bathrooms, parking, and furnishing status.

---

## 📂 Project Structure
House_Price_Prediction_App/
│
├── app.py # Streamlit web application
├── model.pkl # Trained ML model
├── columns.pkl # Feature columns used during training
├── requirements.txt # Project dependencies
├── House_Price_Prediction_ML.ipynb # Model training notebook (Google Colab)
└── README.md


---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Google Colab
- VS Code
- GitHub

---

## 🔬 Model Training
- The dataset was cleaned and preprocessed in Google Colab.
- Categorical features were converted using one-hot encoding.
- The dataset was split into training and testing sets.
- A **Linear Regression** model was trained to predict house prices.
- The trained model was saved as `model.pkl` and feature columns as `columns.pkl`.

---

## 🌐 Streamlit Web Application
- The Streamlit app takes user inputs through a simple UI.
- Inputs are processed and aligned with trained feature columns.
- The trained model predicts the house price in real-time.

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone <your-github-repo-link>
cd House_Price_Prediction_App
