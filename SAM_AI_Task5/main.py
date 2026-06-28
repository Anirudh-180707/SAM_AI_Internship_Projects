import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load training dataset
train_df = pd.read_csv(
    "train_data.txt",
    sep=" ::: ",
    engine="python",
    header=None,
    names=["ID", "Genre", "Description"]
)

# Load test dataset with labels
test_df = pd.read_csv(
    "test_data_solution.txt",
    sep=" ::: ",
    engine="python",
    header=None,
    names=["ID", "Genre", "Description"]
)

# Remove missing values
train_df = train_df.dropna()
test_df = test_df.dropna()

# Features and labels
X_train = train_df["Description"]
y_train = train_df["Genre"]

X_test = test_df["Description"]
y_test = test_df["Genre"]

# Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train the model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Predict genres
predictions = model.predict(X_test)

# Display results
print("=" * 60)
print("Movie Genre Classification")
print("=" * 60)

print(f"Model Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# User Prediction
while True:

    description = input("\nEnter a movie description:\n> ")

    description_vector = vectorizer.transform([description])

    prediction = model.predict(description_vector)[0]

    print(f"\nPredicted Genre: {prediction}")

    choice = input("\nPredict another movie? (y/n): ")

    if choice.lower() != "y":
        print("\nThank you for using Movie Genre Classification!")
        break