# Task 2 - Sentiment Analysis

## Overview

This project implements a **Sentiment Analysis** system using **Machine Learning** and **Natural Language Processing (NLP)**. The model analyzes textual data and predicts whether the sentiment expressed in a sentence is **Positive**, **Negative**, or **Neutral** using **TF-IDF Vectorization** and **Logistic Regression**.

---

## Objective

The objective of this project is to build a machine learning model capable of understanding the sentiment behind text, enabling automatic classification of user opinions and reviews.

---

## Features

* Predicts **Positive**, **Negative**, or **Neutral** sentiment
* Uses **TF-IDF Vectorization** for text feature extraction
* Trains a **Logistic Regression** classifier
* Displays model accuracy and classification report
* Allows users to analyze custom sentences through the console

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Logistic Regression

---

## Project Structure

```text
Task2_Sentiment_Analysis/
│
├── twitter_training.csv
├── twitter_validation.csv
├── main.py
└── README.md
```

---

## Dataset

**Dataset Used:** Twitter Entity Sentiment Analysis Dataset

**Kaggle Link:**
https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis

Dataset Files:

```text
twitter_training.csv
twitter_validation.csv
```

Dataset Columns:

| Column    | Description                 |
| --------- | --------------------------- |
| ID        | Tweet ID                    |
| Entity    | Company/Product Name        |
| Sentiment | Positive, Negative, Neutral |
| Text      | Tweet Content               |

---

## Machine Learning Workflow

1. Load the training and validation datasets.
2. Remove missing values.
3. Filter the dataset to keep only Positive, Negative, and Neutral sentiments.
4. Convert text into numerical features using **TF-IDF Vectorization**.
5. Train the model using **Logistic Regression**.
6. Evaluate the model on the validation dataset.
7. Predict the sentiment of user-entered sentences.

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
I absolutely love this product. It exceeded all my expectations!
```

Output:

```text
Predicted Sentiment: Positive
```

---

### Example 2

Input:

```text
The product arrived damaged, and I am extremely disappointed.
```

Output:

```text
Predicted Sentiment: Negative
```

---

## Expected Output

The program displays:

* Model Accuracy
* Classification Report
* Interactive Sentiment Prediction

Example:

```text
==================================================
Twitter Sentiment Analysis
==================================================
Model Accuracy: 92.45%

Enter a sentence:
> This product is amazing!

Predicted Sentiment: Positive
```

---

## Future Enhancements

* Add a graphical user interface (GUI).
* Deploy the model as a web application using Flask or Streamlit.
* Improve accuracy using deep learning models such as LSTM or BERT.
* Support multilingual sentiment analysis.

---

## Author

**Anirudh L**

Machine Learning Internship – **SAM AI Technologies**
