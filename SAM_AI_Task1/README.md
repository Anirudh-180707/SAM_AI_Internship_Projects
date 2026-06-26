# Task 1 - Spam SMS Detection

## Overview

This project implements a **Spam SMS Detection** system using **Machine Learning** and **Natural Language Processing (NLP)**. The model classifies SMS messages as either **Spam** or **Ham (Legitimate)** by converting text into numerical features using **TF-IDF Vectorization** and training a **Multinomial Naive Bayes** classifier.

---

## Objective

The objective of this project is to build a machine learning model capable of automatically identifying unwanted spam messages, helping users filter fraudulent or promotional SMS messages from genuine ones.

---

## Features

* Classifies SMS messages as **Spam** or **Ham**
* Uses **TF-IDF Vectorization** for text feature extraction
* Trains a **Multinomial Naive Bayes** classifier
* Displays model accuracy and classification report
* Allows users to test custom SMS messages through the console

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Multinomial Naive Bayes

---

## Project Structure

```text
Task1_Spam_SMS_Detection/
│
├── spam.csv
├── main.py
└── README.md
```

---

## Dataset

Dataset Used: **SMS Spam Collection Dataset**

Dataset File:

```text
spam.csv
```

Dataset Columns:

| Column | Description      |
| ------ | ---------------- |
| v1     | Label (ham/spam) |
| v2     | SMS Message      |

**Dataset Source:**
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

---

## Machine Learning Workflow

1. Load the SMS dataset.
2. Select the required columns.
3. Convert labels (`ham`, `spam`) into numeric values.
4. Transform SMS text using **TF-IDF Vectorization**.
5. Split the dataset into training and testing sets.
6. Train a **Multinomial Naive Bayes** classifier.
7. Evaluate the model using accuracy and classification metrics.
8. Predict whether user-entered SMS messages are Spam or Ham.

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

## Sample Inputs

### Example 1

Input:

```text
Congratulations! You have won ₹50,000. Click here to claim now.
```

Output:

```text
Prediction: SPAM
```

---

### Example 2

Input:

```text
Hey, are we meeting at 6 PM today?
```

Output:

```text
Prediction: HAM
```

---

## Expected Output

The program displays:

* Model Accuracy
* Classification Report
* Interactive SMS Prediction

Example:

```text
==================================================
Spam SMS Detection
==================================================
Model Accuracy: 98.12%

Enter an SMS message
> Free recharge available. Click here!

Prediction: SPAM
```

---

## Future Enhancements

* Add a graphical user interface (GUI).
* Deploy the model as a web application using Flask or Streamlit.
* Improve prediction accuracy using advanced NLP techniques.
* Support multiple languages for spam detection.

---

## Author

**Anirudh L**

Machine Learning Internship - **SAM AI Technologies**
