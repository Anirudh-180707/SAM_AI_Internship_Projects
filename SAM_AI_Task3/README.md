# Task 3 - Restaurant Recommendation System

## Overview

This project implements a **Restaurant Recommendation System** using Python. The system recommends restaurants based on the cuisine entered by the user. It utilizes restaurant information such as ratings, votes, location, and approximate cost to provide the best recommendations.

---

## Objective

The objective of this project is to build a simple recommendation system that helps users discover restaurants matching their preferred cuisine using real-world restaurant data.

---

## Features

* Search restaurants by cuisine.
* Displays the top recommended restaurants.
* Shows restaurant name, location, cuisine, rating, votes, and approximate cost.
* Sorts recommendations based on rating and popularity.
* Interactive command-line interface.

---

## Technologies Used

* Python
* Pandas

---

## Project Structure

```text
Task3_Restaurant_Recommendation/
│
├── zomato.csv
├── main.py
└── README.md
```

---

## Dataset

**Dataset Used:** Zomato Restaurants Dataset

**Kaggle Link:**
https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants

**Dataset File:**

```text
zomato.csv
```

> **Note:** The dataset is too large to upload to this repository. Please download the dataset from the Kaggle link above and place the `zomato.csv` file in the project directory before running the application.

---

## Workflow

1. Load the restaurant dataset.
2. Clean the rating and cost columns.
3. Remove missing values.
4. Accept a cuisine from the user.
5. Filter restaurants matching the selected cuisine.
6. Sort recommendations by rating and number of votes.
7. Display the top recommended restaurants.

---

## Installation

Install the required library:

```bash
pip install pandas
```

---

## Running the Project

```bash
python main.py
```

---

## Sample Input

**Input**

```text
North Indian
```

**Output**

```text
Restaurant : ABC Restaurant
Location   : Koramangala
Cuisine    : North Indian, Chinese
Rating     : 4.5/5
Votes      : 2150
Cost for Two: ₹800
```

---

## Future Enhancements

* Add filtering by location.
* Recommend restaurants based on budget.
* Add cuisine and rating filters together.
* Develop a graphical user interface using Tkinter or Streamlit.

---

## Author

**Anirudh L**

Machine Learning Internship – **SAM AI Technologies**
