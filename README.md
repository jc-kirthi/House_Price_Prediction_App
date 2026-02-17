# 🏠 House Price Prediction using Machine Learning & Streamlit

## 📌 Project Overview
This project is an end-to-end Machine Learning application that predicts house prices based on key housing features.
The model was trained using Python and scikit-learn in Google Colab and deployed as an interactive web application
using Streamlit.

This project demonstrates the **complete ML lifecycle**: data preprocessing, model training, serialization,
deployment, debugging, and cloud hosting.

---

## 🧠 Problem Statement
To build a machine learning model that can accurately predict house prices based on housing characteristics such as:
- Area (sq ft)
- Number of bedrooms and bathrooms
- Parking availability
- Road access
- Furnishing status
- Location preference

---

## 📂 Project Structure
House_Price_Prediction_App/

├── app.py # Streamlit web application

├── model.pkl # Trained ML model

├── columns.pkl # Feature columns used during training

├── requirements.txt # Project dependencies

├── House_Price_Prediction_ML.ipynb # Model training notebook (Google Colab)

└── README.md # Project documentation

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
```


## ⚠️ Difficulties Faced

- **Library Version Mismatch:**  
  Model trained in Google Colab used a different `scikit-learn` version than deployment, causing runtime issues.  
  **Solution:** Re-trained and re-serialized the model using a compatible version.

- **Dependency Conflicts:**  
  Incompatible Streamlit and Altair versions caused application crashes.  
  **Solution:** Fixed by properly managing dependencies in `requirements.txt`.

- **Python Version Differences:**  
  Streamlit Cloud runs on Python 3.13, where some deprecated modules are removed.  
  **Solution:** Updated to Python-3.13-compatible library versions.

- **Silent Deployment Errors:**  
  Initial deployments showed blank screens with no visible errors.  
  **Solution:** Debugged using Streamlit Cloud logs and added safer runtime handling.

- **Git Synchronization Issues:**  
  Push failures occurred due to remote changes during deployment.  
  **Solution:** Pulled, merged, and synchronized Git history correctly.

---




