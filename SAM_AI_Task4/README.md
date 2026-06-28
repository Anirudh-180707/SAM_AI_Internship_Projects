# Task 4 - Credit Card Fraud Detection

## Overview

This project implements a **Credit Card Fraud Detection** system using **Machine Learning**. The model is trained to classify credit card transactions as either **Legitimate** or **Fraudulent** using a **Random Forest Classifier**. The application also provides an interactive console interface to test sample transactions.

---

## Objective

The objective of this project is to develop a machine learning model capable of identifying fraudulent credit card transactions, helping improve financial security and reduce fraud.

---

## Features

* Detects fraudulent and legitimate credit card transactions.
* Uses a **Random Forest Classifier** for classification.
* Displays model accuracy and a classification report.
* Interactive console interface for testing transactions.
* Optimized for faster execution using a sampled dataset.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Random Forest Classifier

---

## Project Structure

```text
Task4_Credit_Card_Fraud_Detection/
│
├── creditcard.csv
├── main.py
└── README.md
```

---

## Dataset

**Dataset Used:** Credit Card Fraud Detection Dataset

**Kaggle Link:**

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

**Dataset File:**

```text
creditcard.csv
```

> **Note:** The dataset is too large to upload to this GitHub repository. Please download the dataset from the Kaggle link above and place the `creditcard.csv` file inside the project directory before running the application.

---

## Machine Learning Workflow

1. Load the credit card transaction dataset.
2. Select the transaction features and target labels.
3. Split the dataset into training and testing sets.
4. Train the model using the **Random Forest Classifier**.
5. Evaluate the model using accuracy and classification metrics.
6. Allow users to test legitimate and fraudulent transactions through the console.

---

## Installation

Install the required libraries:

```bash
pip install pandas scikit-learn
```

---

## Running the Project

```bash
python main.py
```

---

## Sample Execution

### Test Legitimate Transaction

**Input**

```text
y
1
```

**Output**

```text
Prediction Result
Legitimate Transaction
```

---

### Test Fraudulent Transaction

**Input**

```text
y
2
```

**Output**

```text
Prediction Result
Fraudulent Transaction
```

---

## Expected Output

The program displays:

* Model Accuracy
* Classification Report
* Interactive Fraud Detection

Example:

```text
============================================================
Credit Card Fraud Detection
============================================================
Model Accuracy: 99.95%

Would you like to test a transaction? (y/n): y

1. Test Legitimate Transaction
2. Test Fraudulent Transaction

Choose an option (1/2): 2

Prediction Result
Fraudulent Transaction
```

---

## Future Enhancements

* Train the model on the complete dataset for improved performance.
* Implement additional machine learning algorithms such as XGBoost or LightGBM.
* Develop a graphical user interface (GUI).
* Deploy the model as a web application using Flask or Streamlit.
* Perform real-time fraud detection using live transaction data.

---

## Author

**Anirudh L**

Machine Learning Internship – **SAM AI Technologies**
