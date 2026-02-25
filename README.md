# 💳 Online Payments Fraud Detection using Machine Learning

A Machine Learning based web application that detects fraudulent online payment transactions using classification algorithms.

This project analyzes transaction details and predicts whether a transaction is **Fraudulent** or **Legitimate**.

---

## 🚀 Live Demo
https://online-payment-fraud-detection-using-ml.onrender.com


 


---

## 📌 Project Overview

Online payment systems are highly vulnerable to fraudulent transactions.  
This project builds a Machine Learning model trained on a large transaction dataset to detect fraud with high precision and recall.

The application allows users to:

- Enter transaction details through a web interface
- Analyze the input using a trained ML model
- Display prediction results instantly
  
- Handles highly imbalanced dataset
- Focuses on Recall for fraud detection
- Industry-level evaluation metrics
- Deployed web application
- Real-time fraud prediction

---

---

## 📊 Dataset

- Source: Kaggle – PaySim Fraud Detection Dataset
- Total Transactions: 6+ Million
- Fraud Percentage: ~0.13% (Highly Imbalanced Dataset)

---

## 🔍 Project Workflow

### 1️⃣ Data Collection
- Imported dataset from Kaggle

### 2️⃣ Data Preprocessing
- Removed unnecessary columns
- Checked for null values
- Label encoded categorical features
- Handled class imbalance using class weights

### 3️⃣ Exploratory Data Analysis
- Univariate Analysis
- Bivariate Analysis
- Correlation Heatmap
- Fraud Distribution Analysis

### 4️⃣ Model Building
Trained and compared multiple models:

- Random Forest
- Decision Tree
- Extra Trees
- XGBoost
- Support Vector Machine

### 5️⃣ Model Evaluation
Due to extreme class imbalance, **Recall and F1-score** were prioritized over Accuracy.

Final Model Performance (Fraud Class):
- Precision: 90%
- Recall: 87%
- F1-score: 89%

### 6️⃣ Model Saving
- Model saved using Joblib

### 7️⃣ Web Application
- Frontend: HTML
- Backend: Flask
- Deployment: Render

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- Gunicorn
- HTML
- Render (Deployment)

---

## 📂 Project Structure
fraud-detection-app/
│
├── app.py

├── fraud_model.pkl

├── requirements.txt

├── Procfile

├── README.md

└── templates/
└── index.html

---



## 📈 Future Improvements

- Add probability score output
- Improve UI design
- Use SMOTE for imbalance handling
- Deploy with Docker
- Add user authentication

---
