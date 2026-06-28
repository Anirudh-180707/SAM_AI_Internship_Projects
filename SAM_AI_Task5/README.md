# Task 5 - Movie Genre Classification

## Overview

This project implements a **Movie Genre Classification** system using **Machine Learning** and **Natural Language Processing (NLP)**. The model predicts the genre of a movie based on its plot description using **TF-IDF Vectorization** and **Logistic Regression**.

---

## Objective

The objective of this project is to build a machine learning model capable of automatically classifying movie genres from textual plot descriptions.

---

## Features

* Predicts movie genres from plot descriptions.
* Uses **TF-IDF Vectorization** for text feature extraction.
* Trains a **Logistic Regression** classifier.
* Displays model accuracy and a classification report.
* Interactive command-line interface for predicting genres of custom movie descriptions.

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
Task5_Movie_Genre_Classification/
│
├── train_data.txt
├── test_data_solution.txt
├── main.py
└── README.md
```

---

## Dataset

**Dataset Used:** IMDb Movie Genre Classification Dataset

**Kaggle Link:**

https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb

**Dataset Files:**

```text
train_data.txt
test_data_solution.txt
```

> **Note:** The dataset files are too large to upload to this GitHub repository. Please download the dataset from the Kaggle link above and place the `train_data.txt` and `test_data_solution.txt` files in the project directory before running the application.

---

## Machine Learning Workflow

1. Load the training and testing datasets.
2. Remove missing values.
3. Convert movie descriptions into numerical features using **TF-IDF Vectorization**.
4. Train the model using **Logistic Regression**.
5. Evaluate the model using accuracy and classification metrics.
6. Predict the genre of user-entered movie descriptions.

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

## Sample Input

### Example 1

**Input**

```text
A superhero fights dangerous criminals to save the city from destruction.
```

**Output**

```text
Predicted Genre: action
```

---

### Example 2

**Input**

```text
Two college students slowly fall in love despite many misunderstandings.
```

**Output**

```text
Predicted Genre: romance
```

---

## Expected Output

The program displays:

* Model Accuracy
* Classification Report
* Interactive Movie Genre Prediction

Example:

```text
============================================================
Movie Genre Classification
============================================================
Model Accuracy: 58.36%

Enter a movie description:
> A detective investigates a mysterious murder.

Predicted Genre: thriller
```

---

## Notes

* **Dataset Availability:** The dataset is not included in this repository because it exceeds GitHub's file size limits. Download it from the Kaggle link above before running the project.
* **Model Accuracy:** An accuracy of around **55%–60%** is expected for this implementation. The IMDb dataset contains **27 different movie genres**, with an imbalanced distribution where some genres have significantly more samples than others. This project uses a baseline **TF-IDF + Logistic Regression** model, which typically achieves this level of accuracy on the dataset. More advanced deep learning models such as **BERT**, **RoBERTa**, or transformer-based architectures can achieve higher accuracy but require greater computational resources.

---

## Future Enhancements

* Improve prediction accuracy using transformer-based NLP models such as BERT or RoBERTa.
* Develop a graphical user interface (GUI).
* Deploy the model as a web application using Flask or Streamlit.
* Support multi-label genre prediction for movies belonging to multiple genres.
* Add confidence scores for each predicted genre.

---

## Author

**Anirudh L**

Machine Learning Internship – **SAM AI Technologies**
