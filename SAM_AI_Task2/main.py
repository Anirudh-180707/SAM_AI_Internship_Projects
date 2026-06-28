import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load training dataset
train_df = pd.read_csv(
    "twitter_training.csv",
    header=None,
    names=["ID", "Entity", "Sentiment", "Text"]
)

# Load validation dataset
test_df = pd.read_csv(
    "twitter_validation.csv",
    header=None,
    names=["ID", "Entity", "Sentiment", "Text"]
)

# Remove missing values
train_df = train_df.dropna()
test_df = test_df.dropna()

# Keep only Positive, Negative, and Neutral sentiments
train_df = train_df[train_df["Sentiment"].isin(["Positive", "Negative", "Neutral"])]
test_df = test_df[test_df["Sentiment"].isin(["Positive", "Negative", "Neutral"])]

# Features and labels
X_train = train_df["Text"]
y_train = train_df["Sentiment"]

X_test = test_df["Text"]
y_test = test_df["Sentiment"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english")

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
print("=" * 50)
print("Twitter Sentiment Analysis")
print("=" * 50)
print(f"Model Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# User Testing
while True:
    print("\nEnter a sentence:")
    text = input("> ")

    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]

    print(f"\nPredicted Sentiment: {prediction}")

    choice = input("\nAnalyze another sentence? (y/n): ")

    if choice.lower() != "y":
        print("\nThank you for using the Sentiment Analysis System!")
        break