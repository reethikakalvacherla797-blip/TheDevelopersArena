# Feature Engineering Documentation - Customer Churn Prediction

## 🔹 Objective
Feature engineering was performed to create new meaningful features that improve model performance.

---

## 🔹 Created Features

### 1. AvgCharges
- Formula:
  TotalCharges / (Tenure + 1)
- Purpose:
  Represents average spending per month.

---

### 2. TenureGroup
- Formula:
  Tenure // 12
- Purpose:
  Groups customers based on yearly tenure.

---

### 3. HighSpender
- Condition:
  MonthlyCharges > 0.5 (after scaling)
- Purpose:
  Identifies high-paying customers.

---

### 4. ChargesPerTenure
- Formula:
  TotalCharges / (Tenure + 1)
- Purpose:
  Measures spending efficiency.

---

### 5. LongTermCustomer
- Condition:
  Tenure > 0.3 (scaled)
- Purpose:
  Identifies loyal customers.

---

### 6. ValueCustomer
- Condition:
  TotalCharges > 0
- Purpose:
  Identifies customers contributing revenue.

---

## 🔹 Importance of Feature Engineering
- Improves model accuracy
- Captures hidden patterns
- Helps in better decision making

---

## 🔹 Feature Selection

### Methods Used:
1. Correlation Analysis
2. Random Forest Feature Importance

---

## 🔹 Final Feature Set
Includes:
- Original features
- Engineered features
- Encoded categorical features

---

## 🔹 Conclusion
Feature engineering significantly enhanced the dataset by adding meaningful insights and improving predictive performance.