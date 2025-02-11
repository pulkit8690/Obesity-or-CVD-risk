# Obesity & CVD Risk Prediction

![App Banner](Images/banner.png)

🚀 **Live App:** [Obesity & CVD Risk Prediction](https://obesity-cvd-risk-prediction.streamlit.app/)

## 📌 Overview
This **Obesity & Cardiovascular Disease (CVD) Risk Prediction** project is a **Streamlit-based web application** that helps users assess their risk of obesity and related health issues based on their lifestyle habits, diet, and physical activity.

## ✨ Features
- 🌍 **User-Friendly Interface** – Multi-step form with progress tracking.
- 🔍 **Predicts Obesity Level** – Uses a trained **Machine Learning Model**.
- 📊 **Analyzes Eating & Physical Activity** – Includes factors like diet, exercise, and technology usage.
- ⚡ **Fast & Efficient** – Optimized using caching techniques.
- 📩 **Deployed on Streamlit Cloud** – Accessible anywhere!

---

## 🏗️ Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python, Pandas, Joblib
- **Machine Learning:** Scikit-learn
- **Deployment:** Streamlit Cloud

---

## 📂 Project Structure
```
📦 Obesity-CVD-Prediction
│-- .devcontainer/      # Development container settings
│-- .git/               # Git repository files
│-- app/                # Streamlit application
│-- data/               # Dataset storage
│-- Images/             # UI assets and banners
│-- Model/              # Pretrained ML model
│-- Notebook/           # Jupyter notebooks
│-- requirements.txt    # Project dependencies
│-- README.md           # Documentation (this file)
```

---

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/pulkit8690/Obesity-or-CVD-risk.git
cd Obesity-CVD-Prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app/app.py
```

---

## 📊 Dataset Information
- **Source:** [Kaggle](https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster)
- **Features Include:**
  - Gender, Age, Height, Weight
  - Eating habits (Vegetable intake, High-calorie food consumption)
  - Physical Activity Frequency
  - Daily water intake, Alcohol consumption
  - Transportation mode
- **Target Variable:** NObeyesdad                      

---

## 🎯 Machine Learning Model
- **Best Model:** Random Forest
- **Model Selection Process:**
  - **Logistic Regression:** Initially chosen for simplicity but performed poorly due to assuming a linear relationship.
  - **Decision Trees:** Improved interpretability but suffered from overfitting.
  - **Support Vector Machine (SVM):** Worked decently but was computationally expensive and struggled with large categorical feature spaces.
  - **Random Forest:** Provided the best balance of accuracy, interpretability, and robustness by averaging multiple decision trees, leading to the best trade-off between accuracy and generalization.

- **Preprocessing:**
  - **Data Loading and Checking Key Aspects** – Inspecting missing values, distributions, and correlations.
  - **OneHotEncoder:** Converts categorical (string) variables into numerical format.
  - **PowerTransformer:** Applies power transformations (like Box-Cox or Yeo-Johnson) to make data more normally distributed, reducing skewness in numerical features.

- **Model Performance:** 97.85% Accuracy

---



## 🤝 Contributing
Feel free to **fork** this repository and submit **pull requests**. Any contributions to improve accuracy, UI, or add new features are welcome!

### 🔗 Connect With Me:
📧 Email: [pulkitarora8690@gmail.com](mailto:pulkitarora8690@gmail.com)  
🌍 GitHub: [pulkit8690](https://github.com/pulkit8690)  
🌐 LinkedIn: [Pulkit Arora](https://www.linkedin.com/in/pulkit-arora-731b17227/)

---


🚀 **Made with ❤️ by [Pulkit Arora]** 🚀
