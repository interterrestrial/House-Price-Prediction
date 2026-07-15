# 🏠 House Price Prediction

An end-to-end Machine Learning project that predicts residential house prices based on various property features such as area, neighborhood, quality, number of rooms, garage capacity, and more.

This project is designed as a comprehensive learning journey through the complete Machine Learning workflow—from data exploration and preprocessing to model building, evaluation, explainability, and deployment.

---

## 📌 Project Overview

House prices are influenced by numerous factors, making price estimation a complex regression problem. The objective of this project is to build a predictive model that accurately estimates the selling price of a house using historical housing data.

Rather than focusing solely on model accuracy, this project emphasizes understanding the complete machine learning pipeline and following industry best practices.

---

## 🎯 Objectives

* Perform comprehensive Exploratory Data Analysis (EDA)
* Clean and preprocess real-world housing data
* Engineer meaningful features
* Train and compare multiple regression models
* Evaluate model performance using various metrics
* Interpret model predictions using explainable AI techniques
* Deploy the trained model as an interactive web application

---

## 📂 Dataset

**Dataset:** Ames Housing Dataset (from Kaggle)  
**Source:** [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview)

The dataset contains detailed information about residential homes, including structural characteristics, location, amenities, and sale prices.

### Features include

* Lot Area
* Overall Quality
* Overall Condition
* Year Built
* Living Area
* Number of Bedrooms
* Number of Bathrooms
* Garage Capacity
* Basement Area
* Neighborhood
* Exterior Material
* Heating System
* Kitchen Quality
* And many more...

**Target Variable**

* SalePrice

---

## 🛠️ Tech Stack

### Machine Learning & Data Science
* **Language:** Python
* **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, XGBoost, SHAP, Joblib

### Backend API
* **Framework:** Flask
* **Features:** Flask-CORS for cross-origin requests, RESTful API endpoint (`/predict`) for model inference

### Frontend Web Application
* **Framework:** Next.js (App Router)
* **Language:** TypeScript
* **Styling:** Vanilla CSS (Glassmorphism design)

### Development Environment
* **Tools:** Jupyter Notebook, Git, GitHub

---

## 📁 Project Structure

```text
house-price-prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Data_Preprocessing.ipynb
│   ├── 05_Model_Training.ipynb
│   ├── 06_Hyperparameter_Tuning.ipynb
│   ├── 07_Model_Evaluation.ipynb
│   ├── 08_Model_Explainability.ipynb
│   └── 09_Inference.ipynb
│
├── models/
│   ├── tuned_gradient_boosting.pkl
│   ├── X_train_encoded.pkl
│   └── scaler.pkl
│
├── frontend/             # Next.js TypeScript Frontend
│   ├── src/app/
│   │   ├── page.tsx      # Main UI
│   │   ├── globals.css   # Glassmorphism styling
│   │   └── layout.tsx
│   └── package.json
│
├── app.py                # Flask Backend API
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📖 Machine Learning Workflow

The project follows the standard machine learning pipeline:

1. Data Collection
2. Data Exploration
3. Exploratory Data Analysis
4. Data Cleaning
5. Handling Missing Values
6. Outlier Detection
7. Feature Engineering
8. Feature Encoding
9. Feature Scaling
10. Model Training
11. Hyperparameter Tuning
12. Model Evaluation
13. Model Explainability
14. Model Deployment

---

## 🤖 Models Evaluated

The following regression algorithms were trained and compared:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor (Selected Model)
* XGBoost Regressor

The Gradient Boosting Regressor was selected as the best-performing model based on evaluation metrics.

---

## 📊 Evaluation Metrics

The models were evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🔍 Explainable AI

To understand how the model makes predictions, SHAP (SHapley Additive exPlanations) was used to:

* Identify important features (e.g., Overall Quality, Total Square Footage, Year Built)
* Explain individual predictions using waterfall plots
* Visualize feature impact and improve model transparency

---

## 🚀 Future Improvements

* Docker containerization
* CI/CD pipeline
* MLflow experiment tracking
* Model monitoring

---

## 🌐 Live Demo

Try the deployed application:

https://house-price-prediction-tan-omega.vercel.app/

--

## 📚 Learning Outcomes

This project demonstrates practical experience with:

* Exploratory Data Analysis
* Data Preprocessing
* Feature Engineering
* Regression Algorithms
* Model Evaluation
* Explainable AI
* Machine Learning Pipelines
* Full-Stack Model Deployment (Flask + Next.js)

---

## 👨‍💻 Author

**Deepak Mishra**

If you found this project helpful, consider giving the repository a ⭐.
