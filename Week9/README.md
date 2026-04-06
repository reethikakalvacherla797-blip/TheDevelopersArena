# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project aims to build a machine learning model to predict house prices based on features such as area, number of bedrooms, bathrooms, age of the property, and location.

The model helps estimate property prices and demonstrates the practical implementation of machine learning concepts.

---

## 🎯 Objectives

* Understand basic machine learning concepts
* Implement Linear Regression using scikit-learn
* Perform data preprocessing and feature engineering
* Evaluate model performance using standard metrics
* Visualize predictions vs actual values

---

## 📊 Dataset Information

* Dataset: House Prices Dataset
* Rows: 300
* Columns: 5

### Features:

* Area
* Bedrooms
* Bathrooms
* Age
* Location
* Price (Target Variable)

---

## ⚙️ Tech Stack

* Python
* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* Jupyter Notebook

---

## 📂 Project Structure

```
House-Price-Prediction/
│
├── house_price_prediction.ipynb
├── house_prices.csv
├── model_evaluation_report.md
├── requirements.txt
├── predictions_vs_actual.png
└── README.md
```

---

## 🧹 Data Preprocessing

* Removed unnecessary columns (Property_ID)
* Handled missing values
* Converted categorical variables using One-Hot Encoding
* Split data into training and testing sets

---

## 🤖 Model Used

### Linear Regression

* Simple and interpretable model
* Suitable for predicting continuous values

---

## 📈 Model Evaluation

The model performance was evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

### Example Results:

```
MAE: 45200  
MSE: 3.2e9  
R² Score: 0.78  
```

---

## 📊 Visualization

A scatter plot is used to compare actual vs predicted prices.

* X-axis → Actual Prices
* Y-axis → Predicted Prices

---

## 🚀 How to Run the Project

### 1. Clone the repository

```
git clone <your-repo-link>
cd House-Price-Prediction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run Jupyter Notebook

```
jupyter notebook
```

### 4. Open and run:

```
house_price_prediction.ipynb
```

---

## 📸 Output

* Model predictions
* Evaluation metrics
* Visualization graph (`predictions_vs_actual.png`)

---

## 🔍 Key Insights

* Area is the most influential feature
* Location significantly impacts price
* More bedrooms and bathrooms increase house value

---

## ⚠️ Limitations

* Small dataset (300 rows)
* Limited features
* Linear model may not capture complex relationships

---

## 🔮 Future Improvements

* Use advanced models (Random Forest, Gradient Boosting)
* Add more features (e.g., amenities, location details)
* Hyperparameter tuning
* Use larger datasets

