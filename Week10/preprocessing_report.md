# Data Preprocessing Report - Customer Churn Prediction

## 🔹 Project Overview
The goal of this project is to preprocess customer data and prepare it for machine learning to predict customer churn.

---

## 🔹 Dataset Description
The dataset contains the following features:
- Tenure
- MonthlyCharges
- TotalCharges
- PaperlessBilling
- SeniorCitizen
- Churn (Target Variable)
- Pre-encoded categorical variables for Contract and PaymentMethod

---

## 🔹 Data Cleaning
- No missing values were found in the dataset.
- Data types were verified and corrected where necessary.

---

## 🔹 Handling Categorical Data
- The dataset already contained one-hot encoded columns:
  - Contract_Month-to-month
  - Contract_One year
  - Contract_Two year
  - PaymentMethod_Bank Transfer
  - PaymentMethod_Credit Card
  - PaymentMethod_Electronic Check
- Therefore, no additional encoding was required.

---

## 🔹 Feature Scaling
Two scaling techniques were applied:

### 1. Min-Max Scaling
- Applied to:
  - Tenure
  - MonthlyCharges
- Purpose:
  - To bring values between 0 and 1.

### 2. Standard Scaling
- Applied to:
  - TotalCharges
- Purpose:
  - To normalize data with mean 0 and standard deviation 1.

---

## 🔹 Outlier Detection and Handling

### 1. IQR Method
- Used to detect outliers in MonthlyCharges.
- Removed values outside acceptable range.

### 2. Z-Score Method
- Applied on TotalCharges.
- Removed rows with Z-score > 3.

---

## 🔹 Data Transformation Summary
- Removed unnecessary columns (if any).
- Applied scaling techniques.
- Removed outliers.
- Verified final dataset consistency.

---

## 🔹 Final Output
The dataset is now:
- Cleaned
- Scaled
- Free from major outliers
- Ready for feature engineering and modeling

---

## 🔹 Conclusion
Proper preprocessing improved data quality and ensured better model performance. All steps were carefully applied and validated.
